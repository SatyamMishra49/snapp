from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def check():
    return jsonify({"status": "ok"}), 200

'''
GET urls/
'''
@app.route('/v1/url', methods=['GET'])
def get_urls():
    return jsonify({"message": "short urls"}), 200

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

    if original_url:
        # save the URL to a database
        return jsonify({"message": "URL created", "url": original_url}), 201
    else:
        return jsonify({"error": "Invalid URL"}), 400

app.run(debug=True, port=5000)