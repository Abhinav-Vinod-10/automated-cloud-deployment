
from flask import Flask, jsonify
import time
import os

app = Flask(__name__)

start_time = time.time()

@app.route("/")
def home():
    return jsonify({
        "application": "Automated Cloud Deployment System",
        "status": "Running",
        "version": "1.0.0"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "uptime_seconds": round(time.time() - start_time, 2)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
