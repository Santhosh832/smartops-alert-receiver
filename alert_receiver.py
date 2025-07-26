from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def receive_alert():
    alert = request.json
    print("🔔 Received alert from Prometheus:")
    print(alert)
    
    # TODO: You can add AI interpretation here
    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
