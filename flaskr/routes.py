from flask import Blueprint, render_template
from flaskr.data import fetch_data
from flaskr.analysis import analyze_data

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    api_url = "https://otx.alienvault.com/api/v1/indicators"
    data = fetch_data(api_url)
    common_threats, spikes, analyzed_data = analyze_data(data)
    return render_template('dashboard.html', common_threats=common_threats, spikes=spikes, data=analyzed_data)
