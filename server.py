from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

VERSION_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'version.json')

def load_version():
    with open(VERSION_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    return jsonify({"status": "Painting Heresy Update Server", "ok": True})

@app.route('/version')
def version():
    try:
        return jsonify(load_version())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
