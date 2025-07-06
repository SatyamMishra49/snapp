from flask import Flask, jsonify, render_template
import os
import json
import requests
from flask_sqlalchemy import SQLAlchemy # type: ignore
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()
    pass

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
    
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)