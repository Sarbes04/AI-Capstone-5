from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "AI Security Demo Application"})


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "")

    # Simulated AI response
    response = f"AI received your message: {user_message}"

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)