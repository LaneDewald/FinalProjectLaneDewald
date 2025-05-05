import pandas as pd
import numpy as np

def generate_random_data():
    np.random.seed(0)
    dates = pd.date_range(start='2023-01-01', periods=100)
    threat_types = ['Malware', 'Phishing', 'Ransomware', 'Spyware']
    data = {
        'date': np.random.choice(dates, 100),
        'threat_type': np.random.choice(threat_types, 100),
        'indicator': np.random.rand(100)
    }
    return pd.DataFrame(data)




