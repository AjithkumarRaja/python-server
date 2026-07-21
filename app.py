from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def health():

    return jsonify({
        "status": "UP",
        "service": "Mock Oracle ERP"
    })


@app.route("/api/orders", methods=["POST"])
def create_order():

    # Simulate Oracle ERP being unavailable
    return jsonify({
        "success": False,
        "error": "Mock Oracle ERP is temporarily unavailable"
    }), 503


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
