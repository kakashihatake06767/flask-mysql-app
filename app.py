from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <h1>Automatic Deployment Test </h1>
    <p>Flask Container Running</p>
    <p>Database Host: {os.getenv('DB_HOST')}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
