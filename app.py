from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

EMAIL_ADDRESS = "santhanam832@gmail.com"
EMAIL_PASSWORD = "fffuhegujgiigvbh"
TO_EMAIL = "santhanam832@gmail.com"  # Can be the same or different

@app.route('/alert', methods=['POST'])
def handle_alert():
    data = request.json
    print("Received alert:", data)

    interpretation = interpret_alert(data)
    print("SmartOps AI says:", interpretation)

    # ✉️ Send the interpretation by email
    send_email("SmartOps Alert", interpretation)

    return jsonify({"message": "Alert received", "analysis": interpretation})


def interpret_alert(data):
    if not data or "alerts" not in data or len(data["alerts"]) == 0:
        return "✅ No active alerts. System looks healthy."

    messages = []
    for alert in data["alerts"]:
        name = alert.get("labels", {}).get("alertname", "Unnamed")
        severity = alert.get("labels", {}).get("severity", "unknown")
        desc = alert.get("annotations", {}).get("description", "No description")
        messages.append(f"⚠️ *{name}* (severity: {severity}) – {desc}")

    return "\n".join(messages)


def send_email(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = TO_EMAIL

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print("📧 Email sent successfully.")
    except Exception as e:
        print("❌ Failed to send email:", e)


if __name__ == '__main__':
    app.run(debug=True)



