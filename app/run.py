from flask import Flask, jsonify, request
from connector.helper_func import store_to_db, get_all_urls
from db import p_db, get_url

app = Flask(__name__)


@app.route('/', methods=['GET'])
def check():
    return jsonify({"status": "ok"}), 200

'''
GET urls/
'''
@app.route('/v1/url', methods=['GET'])
def get_urls():
    # urls = get_all_urls()
    urls = get_url()

    if urls is None:
        return jsonify({"error": "Failed to retrieve URLs"}), 500
    return jsonify({"urls": urls}), 200

'''
GET long_urls/
'''
@app.route('/v1/long_url', methods=['GET'])
def get_long_urls():
    return jsonify({"message": "long urls"}), 200

''''
POST urls/
'''
@app.route('/v1/url', methods=['POST'])
def create_url():
    data = request.get_json()
    original_url = data.get('url')

    if not original_url:
        return jsonify({"error": "Invalid URL"}), 400
    else:
        # res = store_to_db(original_url)
        res = p_db(original_url)

        if res:
            print(f"URL stored successfully: {original_url}")
        else:
            print(f"Failed to store URL: {original_url}")
            return jsonify({"error": "Failed to store URL"}), 500
        
        return jsonify({"message": "URL created successfully"}), 201
        

app.run(debug=True, port=5000)