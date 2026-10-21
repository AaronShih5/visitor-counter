from flask import Flask
import redis, os, socket

app = Flask(__name__)
db = redis.Redis(host="redis", port=6379)

@app.route("/")
def home():
    count = db.incr("visits")
    name = os.getenv("APP_NAME", "My App")
    return f"""
    <h1>{name}</h1>
    <p>This page has been visited <b>{count}</b> times.</p>
    <p>Served by container: {socket.gethostname()}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
