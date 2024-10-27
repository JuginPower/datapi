from flask import Flask, jsonify, request
from pathlib import Path
import os
import json

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent.parent

@app.route('/stock', methods=['GET', 'POST', 'DELETE'])
def download_data():

    response = None
    data_path = os.path.join(BASE_DIR, "data.jsonl")

    try:
        if request.method in ['GET', 'POST']:
            data = []
            with open(data_path, "r") as f:
                for line in f:
                    data.append(json.loads(line))

            response = jsonify(data), 200

        elif request.method == 'DELETE':
            os.remove(data_path)
            response = {"response": "Succeed"}, 200

    except FileNotFoundError:
        response = {"response": "No Data"}, 404
    
    return response
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
