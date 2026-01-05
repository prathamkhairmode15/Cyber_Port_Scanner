from flask import Flask, render_template, request, jsonify, send_file
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os

from scanner import scan_ports, detect_os
from db import init_db, save_scan, get_history

app = Flask(__name__)
init_db()

last_report = {}

@app.route("/")
def home():
    history = get_history()
    return render_template("index.html", history=history)

@app.route("/scan", methods=["POST"])
def scan():
    try:
        data = request.get_json(force=True)
        target = data["target"].strip()
        start_port = int(data["start"])
        end_port = int(data["end"])

        osguess = detect_os(target)
        open_ports, tagged = scan_ports(target, start_port, end_port)

        tagged = [{"port": p, "note": n} for (p, n) in tagged]

        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        save_scan(target, osguess, ",".join(map(str, open_ports)), date)

        global last_report
        last_report = {
            "target": target,
            "os": osguess,
            "open_ports": open_ports,
            "tags": tagged,
            "time": date
        }

        return jsonify(last_report)

    except Exception as e:
        print("SCAN ERROR:", e)
        return jsonify({"error": str(e)}), 400

@app.route("/export")
def export():
    filename = f"reports/report_{datetime.now().strftime('%Y%m%d%H%M')}.pdf"

    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(filename)

    content = [
        Paragraph("Port Scan Report", styles["Title"]),
        Spacer(1, 14)
    ]

    for k, v in last_report.items():
        content.append(Paragraph(f"<b>{k}:</b> {v}", styles["BodyText"]))
        content.append(Spacer(1, 8))

    doc.build(content)
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    if not os.path.exists("reports"):
        os.makedirs("reports")
    app.run(debug=True)
