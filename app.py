from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Render!"

@app.route("/hello")
def hello():
    return jsonify({
        "message": "Hello World!",
        "status": "success"
    })

@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({
        "received": data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
