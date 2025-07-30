from flask import Flask
import os

app = Flask(__name__)

# Read VERSION environment variable
version = os.getenv("VERSION", "v1")

@app.route("/")
def home():
    return f"Hello from Monolith App - Version: {version}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
