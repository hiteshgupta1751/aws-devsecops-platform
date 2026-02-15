from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "status": "running",
        "service": "devsecops-platform",
        "time": str(datetime.datetime.utcnow())
    }

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    numbers = data.get("numbers", [])
    
    return jsonify({
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers)/len(numbers) if numbers else 0
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

