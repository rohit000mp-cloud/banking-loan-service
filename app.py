from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/loan")
def loan():
    return jsonify({
        "service": "Loan Service",
        "status": "running",
        "message": "Loan service v2 is available"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
