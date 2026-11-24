import os
import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)

@app.route("/")
def index():
    count = r.incr("visits")
    return f"<h1>Visitor Counter</h1><h2>You are visitor number {count}</h2>"

@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
