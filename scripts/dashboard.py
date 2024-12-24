import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load data
engagement_data = pd.read_csv("engagement_data.csv")
experience_data = pd.read_csv("experience_data.csv")
satisfaction_data = pd.read_csv("satisfaction_data.csv")

# Sidebar navigation
st.sidebar.title("Dashboard Navigation")
page = st.sidebar.selectbox(
    "Select a Page",
    ["User Overview Analysis", "User Engagement Analysis", "Experience Analysis", "Satisfaction Analysis"]
)

# User Overview Analysis
if page == "User Overview Analysis":
    st.title("User Overview Analysis")
    
    # Top 10 handsets
    top_handsets = engagement_data["Handset Type"].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_handsets.values, y=top_handsets.index, palette="viridis", ax=ax)
    ax.set_title("Top 10 Handsets Used by Customers")
    st.pyplot(fig)

    # Top 3 manufacturers
    top_manufacturers = engagement_data["Handset Manufacturer"].value_counts().head(3)
    fig, ax = plt.subplots(figsize=(8, 5))
    top_manufacturers.plot.pie(autopct='%1.1f%%', ax=ax, colors=sns.color_palette("pastel"))
    ax.set_title("Top 3 Handset Manufacturers")
    st.pyplot(fig)

# User Engagement Analysis
elif page == "User Engagement Analysis":
    st.title("User Engagement Analysis")

    # Scatterplot for Session Duration vs Traffic
    fig = px.scatter(
        engagement_data, 
        x="Total Session Duration (ms)", 
        y="Total Traffic (Bytes)", 
        color="Cluster", 
        title="Session Duration vs Traffic by Cluster"
    )
    st.plotly_chart(fig)

    # Average metrics per cluster
    cluster_summary = engagement_data.groupby("Cluster").mean()
    st.bar_chart(cluster_summary[["Session Frequency", "Total Traffic (Bytes)"]])

# Experience Analysis
elif page == "Experience Analysis":
    st.title("Experience Analysis")

    # RTT vs Throughput
    fig = px.scatter(
        experience_data,
        x="Avg RTT DL (ms)",
        y="Avg Throughput DL (kbps)",
        color="Experience Cluster",
        title="RTT vs Throughput by Cluster"
    )
    st.plotly_chart(fig)

    # Correlation Heatmap
    corr = experience_data.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Matrix of Experience Metrics")
    st.pyplot(fig)

# Satisfaction Analysis
elif page == "Satisfaction Analysis":
    st.title("Satisfaction Analysis")

    # Top 10 satisfied customers
    top_10 = satisfaction_data.nlargest(10, "Satisfaction Score")
    st.table(top_10[["MSISDN/Number", "Satisfaction Score"]])

    # Scatterplot for Engagement vs Experience Score
    fig = px.scatter(
        satisfaction_data,
        x="Engagement Score",
        y="Experience Score",
        color="Cluster",
        title="Engagement vs Experience Score"
    )
    st.plotly_chart(fig)

    # Bar chart for satisfaction scores per cluster
    cluster_summary = satisfaction_data.groupby("Cluster").mean()
    fig = px.bar(
        cluster_summary,
        x=cluster_summary.index,
        y="Satisfaction Score",
        title="Average Satisfaction Score per Cluster"
    )
    st.plotly_chart(fig)
