from flask import Flask, request, jsonify

app = Flask(__name__)

current_command = None

@app.route("/")
def home():
    return "TV Remote Server Running"

@app.route("/send", methods=["POST"])
def send():
    global current_command
    data = request.json
    current_command = data["command"]
    return jsonify({"status": "ok"})

@app.route("/get")
def get():
    global current_command
    cmd = current_command
    current_command = None
    return jsonify({"command": cmd})

if __name__ == "__main__":
    app.run()
