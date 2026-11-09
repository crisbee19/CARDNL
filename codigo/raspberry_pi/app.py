from flask import Flask
from flask import render_template

import os
import sqlite3

print("APP DB:")
print(os.path.abspath("neighbornet.db"))

app = Flask(__name__)


@app.route("/")
def home():
    conn = sqlite3.connect("neighbornet.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM requests")
    requests = cursor.fetchall()
    print(requests)

    cursor.execute("SELECT * FROM alerts")
    alerts = cursor.fetchall()
    print(alerts)

    cursor.execute("SELECT * FROM resources")
    resources = cursor.fetchall()
    print(resources)

    cursor.execute("SELECT * FROM deliveries")
    deliveries = cursor.fetchall()
    print(deliveries)

    conn.close()

    return render_template(
        "index.html",
        requests=requests,
        alerts=alerts,
        resources=resources,
        deliveries=deliveries
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
