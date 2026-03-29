import os
import sys
import logging.config
import json
from flask import Flask, request, jsonify
from auth_gateway import config
from auth_gateway.auth import Authenticator

app = Flask(__name__)

logging.config.dictConfig(config.LOGGING_CONFIG)

@app.route('/auth', methods=['POST'])
def auth():
    data = request.json
    if data is None:
        return jsonify({'error': 'missing json payload'}), 400
    if 'username' not in data or 'password' not in data:
        return jsonify({'error': 'missing username or password'}), 400
    authenticator = Authenticator()
    if authenticator.authenticate(data['username'], data['password']):
        return jsonify({'token': authenticator.generate_token()}), 200
    else:
        return jsonify({'error': 'invalid credentials'}), 401

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)