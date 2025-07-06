from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow your file:// page to talk to this server

@app.route('/process', methods=['POST'])
def process_txt():
    uploaded = request.files.get('file')
    if not uploaded or not uploaded.filename.lower().endswith('.txt'):
        return jsonify(error="No .txt file uploaded"), 400

    text = uploaded.read().decode('utf-8', errors='ignore')
    count = len(text.split())
    return jsonify(filename=uploaded.filename, word_count=count)

if __name__ == '__main__':
    app.run(port=5000)
