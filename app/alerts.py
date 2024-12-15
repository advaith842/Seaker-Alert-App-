from flask import Flask, jsonify, request
from metrics import get_system_metrics
from alerts import check_alerts, send_telegram_alert

app = Flask(__name__)

# Replace these with actual values
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

@app.route('/metrics', methods=['GET'])
def metrics():
    system_metrics = get_system_metrics()
    return jsonify(system_metrics)

@app.route('/alerts', methods=['POST'])
def alerts():
    system_metrics = get_system_metrics()
    alert_messages = check_alerts(system_metrics)
    for alert in alert_messages:
        send_telegram_alert(alert, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID)
    return jsonify({"alerts": alert_messages})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
