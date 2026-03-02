import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier

#load the data
st.set_page_config(page_title="Cyber Threat Strategy Optimization Engine", layout="wide")
@st.cache_data
def load_data():
    df = pd.read_csv("cyberthreat_data.csv")

    #best strategy for every attack type
    strategy_cal = df.groupby("Attack Type").apply(
        lambda x: x.loc[x["Incident Resolution Time (in Hours)"].idxmin(), ["Defense Mechanism Used", "Incident Resolution Time (in Hours)"]]
    ).reset_index()

    #overall average for comparison
    avg_time = df.groupby("Attack Type")["Incident Resolution Time (in Hours)"].mean().reset_index()
    avg_time.columns = ["Attack Type", "Avg_Time"]

    return df, strategy_cal, avg_time

df, strategy_cal, avg_time = load_data()

#the interface
st.title("Cyber Threat Strategy Optimization Engine")
st.markdown("---")

col1, col2 = st.columns([1,2])

with col1:
    st.subheader("incident details")
    industry = st.selectbox("Target Industry", df["Target Industry"].unique())
    attack = st.selectbox("Attack Type", df["Attack Type"].unique())
    source = st.selectbox("Attack Source", df["Attack Source"].unique())
    defense = st.selectbox("Defense Mechanism", df["Defense Mechanism Used"].unique())

#prescriptive analysis engine
with col2:
    st.subheader("Strategic Solution")

    #best defense based on historical calculation
    best_attack = strategy_cal[strategy_cal["Attack Type"] == attack].iloc[0]
    best_defense = best_attack["Defense Mechanism Used"]
    best_time = best_attack["Incident Resolution Time (in Hours)"]

    #average time for the particular attack
    averageTime = avg_time[avg_time["Attack Type"] == attack]["Avg_Time"].values[0]

    #time saved
    time_saved = round(averageTime - best_time, 1)

    #metrics
    m1,m2 = st.columns(2)
    m1.metric("Optimal Defense", best_defense)
    m2.metric("Potential Time Saved", f"{time_saved}Hours", delta_color="normal")

    st.markdown("---")

    #chart
    st.write(f"Resolution Time Comparison for {attack}")
    chart_data = pd.DataFrame({
        "Strategy": ["Industry Average", "Recommended path"],
        "Hours": [averageTime, best_time]
    })
    
    fig = px.bar(
        chart_data,
        x="Strategy",
        y="Hours",
        color="Strategy",
        text_auto=".1f",
        color_discrete_map={
            "Industry Average": "#636EFA",
            "Recommended Path": "#00CC96"
        }
    )

    fig.update_layout(
        xaxis_title="",
        yaxis_title="Hours to Resolve",
        showlegend=False,
        margin=dict(l=20, r=20, t=30, b=20),
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

st.success(f""" 
Recommendation: Historically, in incidents involving  **{attack}**, mitigating to **{best_defense}** has reduced the resolution time to as low as **{best_time}** hour.
Compared to average resolution time of **{round(averageTime,1)}hours**, this transition represents a **{round((time_saved/averageTime)*100)}% efficiency gain**""")