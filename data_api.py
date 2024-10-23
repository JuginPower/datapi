from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/scrapy-data')
def download_data():
    # Pfad zur Datei, die gesendet werden soll
    path = "/home/eugen/projects/webcrawler/data.jsonl"

    # Sende die Datei
    response = send_file(path, as_attachment=True)
    
    # Lösche die Datei nach dem Senden
    os.remove(path)

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
