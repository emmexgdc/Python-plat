from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'time': datetime.datetime.now().isoformat(),
        'hostname': socket.gethostname()
    })

@app.route('/api/v1/healthz')
def healthz():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host="0.0.0.0")