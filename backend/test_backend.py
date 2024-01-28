from flask import Flask, jsonify
import csv
from flask_cors import CORS  # Import the CORS module

app = Flask(__name__)
CORS(app)

@app.route('/api/csv', methods=['GET'])
def get_data():
    csv_file_path = 'businesses.csv'
    selected_columns = ['name', 'address', 'city']  # Replace with your actual column names

    data = []

    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            selected_data = {key: row[key] for key in selected_columns}
            data.append(selected_data)

    data = 'a'

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
