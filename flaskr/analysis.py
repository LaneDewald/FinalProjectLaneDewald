import numpy as np
import scipy.cluster.hierarchy as sch

def analyze_data(data):
    common_threats = data['threat_type'].value_counts()
    spikes = data.groupby('date')['threat_type'].count().diff().fillna(0)
    if 'indicator' in data.columns:
        indicators = data['indicator'].values
        linkage_matrix = sch.linkage(indicators, method='ward')
        clusters = sch.fcluster(linkage_matrix, t=1.5, criterion='distance')
        data['cluster'] = clusters
    return common_threats, spikes, data
