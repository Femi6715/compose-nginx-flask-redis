from flask import Flask, jsonify
import os
import redis

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST","localhost"), port=6379, decode_responses=True)

@app.route("/")
def home():
    r.incr("hits")
    return jsonify(service="flask-app", hits=int(r.get("hits") or 0))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
