from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route("/")
def index():
	return jsonify({
		"message": "Hello from Flask + Gunicorn!",
		"worker": os.getenv("WORKER_ID", "unknown")
	})

@app.route("/echo", methods=["POST"])
def echo():
	data = request.json or {}
	return jsonify({"you_sent": data})
