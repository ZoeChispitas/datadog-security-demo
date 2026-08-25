from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "status": "running",
        "environment": "production",
        "version": "1.1.0"
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
