# Prueba: simula un mensaje del ESP32 pidiendo agua para House A.
import sqlite3

house = "House A"
resource = "Water"

conn = sqlite3.connect("neighbornet.db")
cursor = conn.cursor()
cursor.execute(
    """
    INSERT INTO requests
    (house, resource, status)
    VALUES
    (?, ?, ?)
    """,
    (house, resource, "Pending")
)
conn.commit()
conn.close()
print("ESP32 Message Received")
