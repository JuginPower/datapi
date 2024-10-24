from flask import Flask, jsonify, request
import os
import json

app = Flask(__name__)

@app.route('/stock', methods=['GET', 'POST', 'DELETE'])
def download_data():

    response = None
    path = "/home/eugen/Schreibtisch/projects/datapi/data.jsonl"

    try:
        if request.method in ['GET', 'POST']:
            
            with open(path, 'r') as f:
                data = [json.loads(line) for line in f]

            response = jsonify(data), 200

        elif request.method == 'DELETE':
            os.remove(path)
            response = {"response": "Succeed"}, 200

    except FileNotFoundError:
        response = {"response": "No Data"}, 404
    
    return response
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
