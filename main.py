### INF601 - Advanced Programming in Python
### Lane Dewald
### Final Project


import pandas as pd
import requests
import numpy as np
import scipy.cluster.hierarchy as sch
import streamlit as st
from flask import Flask, render_template

# Data Collection Module
def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        print("Failed to fetch data")
        return None

# Analysis Module
def analyze_data(data):
    # Identify most common threat types
    common_threats = data['threat_type'].value_counts()

    # Detect unusual spikes in threat frequency
    spikes = data.groupby('date')['threat_type'].count().diff().fillna(0)

    # Cluster similar threat indicators
    if 'indicator' in data.columns:
        indicators = data['indicator'].values
        linkage_matrix = sch.linkage(indicators, method='ward')
        clusters = sch.fcluster(linkage_matrix, t=1.5, criterion='distance')
        data['cluster'] = clusters
    return common_threats, spikes, data


# Visualization Dashboard
def display_dashboard(common_threats, spikes, data):
    st.title("Cyber Threat Intelligence Dashboard")

    st.header("Top Threat Categories")
    st.bar_chart(common_threats)

    st.header("Threat Frequency Spikes")
    st.line_chart(spikes)

    st.header("Indicators of Compromise")
    st.dataframe(data[['indicator', 'threat_type', 'date', 'cluster']])

    st.sidebar.header("Filters")
    date_filter = st.sidebar.date_input("Date")
    severity_filter = st.sidebar.selectbox("Severity", options=data['severity'].unique())
    region_filter = st.sidebar.selectbox("Region", options=data['region'].unique())
    type_filter = st.sidebar.selectbox("Type", options=data['threat_type'].unique())

    filtered_data = data[
        (data['date'] == date_filter) &
        (data['severity'] == severity_filter) &
        (data['region'] == region_filter) &
        (data['threat_type'] == type_filter)
    ]
    st.dataframe(filtered_data)
