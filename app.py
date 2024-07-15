from flask import Flask, jsonify
import requests
import json
import os

from transform import transform_posting
from retrieve import retrieve_data

app = Flask(__name__)
data = retrieve_data() 

@app.route('/get_position_titles')
def get_position_titles():
    all_position_titles = []
    for posting in data:
        position_title = posting['business_title']
        all_position_titles.append(position_title)
    return jsonify(all_position_titles)

@app.route('/get_lower_bounds_for_compensation')
def get_lower_bounds_for_compensation():
    all_lower_bounds = []
    for posting in data:
        lower_bound = posting['salary_range_from']
        all_lower_bounds.append(lower_bound)
    return jsonify(all_lower_bounds)

@app.route('/get_upper_bounds_for_compensation')
def get_upper_bounds_for_compensation():
    all_upper_bounds = []
    for posting in data:
        upper_bound = posting['salary_range_to']
        all_upper_bounds.append(upper_bound)
    return jsonify(all_upper_bounds)

@app.route('/get_skills')
def get_skills():
    all_skills = []
    for posting in data:
        cleaned_skill_sets = transform_posting(posting)
        all_skills.append(cleaned_skill_sets)
    return jsonify(all_skills)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)
    