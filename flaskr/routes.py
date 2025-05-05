from flask import Blueprint, render_template
from flaskr.analysis import analyze_data
from flaskr.data import generate_random_data

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    data = generate_random_data()
    common_threats, spikes, analyzed_data = analyze_data(data)
    return render_template('dashboard.html', common_threats=common_threats, spikes=spikes, data=analyzed_data)





