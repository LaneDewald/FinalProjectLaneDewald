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
