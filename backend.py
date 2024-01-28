from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# main page
@app.route('/')
def index():
    return render_template('index.html')

# file upload
@app.route('/upload', methods=['POST'])
def upload():
    # check for file
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    # valid filename?
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    #CSV file?
    if file.filename.endswith('.csv'):

        df = pd.read_csv(file)
        result_json = df.to_json(orient='records')

        return jsonify({'result': result_json})
    else:
        return jsonify({'error': 'Invalid file format'})

if __name__ == '__main__':
    app.run(debug=True)
