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

