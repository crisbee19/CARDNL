# Prueba: pide por teclado la casa y el recurso, y guarda la solicitud.
import sqlite3

print()
house = input("House: ")
resource = input("Resource Needed: ")

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

print()
print("Request Added")
