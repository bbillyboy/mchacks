from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route('/api/csv')
def get_data():
    csv = pd.read_csv("username.csv", delimiter=';')
    json_data = csv.to_json(orient='records')
    return json_data

@app.route('/api/data')
def my_profile():
    restaurants = pd.read_csv("businesses.csv", usecols=["latitude","longitude"])
    restaurants_json = restaurants.to_json(orient='records')
    return restaurants_json
