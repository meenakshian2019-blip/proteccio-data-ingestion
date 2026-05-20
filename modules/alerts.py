# modules/alerts.py

def generate_alerts(risk_score):

    alerts = []

    if risk_score >= 80:

        alerts.append({
            "severity": "High",
            "message": "Critical privacy risk detected"
        })

    elif risk_score >= 50:

        alerts.append({
            "severity": "Medium",
            "message": "Moderate privacy risk detected"
        })

    else:

        alerts.append({
            "severity": "Low",
            "message": "Low privacy risk"
        })

    return alerts