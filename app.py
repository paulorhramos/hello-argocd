from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

VERSION = os.getenv('APP_VERSION', 'v2.0.0')

@app.route('/')
def hello():
    return jsonify({
        'message': 'Hello from ArgoCD!',
        'version': VERSION,
        'hostname': socket.gethostname(),
        'environment': os.getenv('ENVIRONMENT', 'production')
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
