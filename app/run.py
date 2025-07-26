from flask import Flask, jsonify


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


app.run(debug=True, port=5000)