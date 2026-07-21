from flask import Flask, request, jsonify
import uuid
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods=["GET"])
def health():
    return jsonify({
        "status": "UP",
        "service": "Mock Oracle ERP"
    })


@app.route("/api/orders", methods=["POST"])
def create_order():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "error": "Invalid JSON request"
        }), 400

    customer = data.get("customer")
    items = data.get("items")

    # Validate customer
    if not customer:
        return jsonify({
            "success": False,
            "error": "Customer information is required"
        }), 400

    if not customer.get("name"):
        return jsonify({
            "success": False,
            "error": "Customer name is required"
        }), 400

    # Validate products
    if not items:
        return jsonify({
            "success": False,
            "error": "At least one product is required"
        }), 400

    # Validate each product
    for item in items:

        if not item.get("productCode"):
            return jsonify({
                "success": False,
                "error": "Product code is required"
            }), 400

        if not item.get("quantity"):
            return jsonify({
                "success": False,
                "error": "Product quantity is required"
            }), 400

    # Generate Oracle Order ID
    oracle_order_id = (
        "ORA-" +
        datetime.now().strftime("%Y%m%d") +
        "-" +
        uuid.uuid4().hex[:8].upper()
    )

    return jsonify({
        "success": True,
        "oracleOrderId": oracle_order_id,
        "status": "CREATED",
        "message": "Order successfully created in Mock Oracle ERP"
    }), 201


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
