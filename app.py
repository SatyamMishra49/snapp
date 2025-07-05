from Flask import Flask, jsonify
import os
import json
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    # Health check endpoint to verify if the service is running.
    
    return jsonify({"status": "ok"}), 200

@app.route('/v1/app', methods=['GET'])
def main_handler():
    try:
        return jsonify({"message": "v1 route running"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)