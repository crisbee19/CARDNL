# Prueba: simula una alerta de inundación de House A.
import sqlite3

conn = sqlite3.connect("neighbornet.db")
cursor = conn.cursor()
cursor.execute(
    """
    INSERT INTO alerts
    (house, event)
    VALUES
    ('House A', 'Flood Detected')
    """
)
conn.commit()
conn.close()
