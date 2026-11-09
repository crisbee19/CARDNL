# Simulador del nodo ESP32.
# Mientras el ESP32 físico y el enlace LoRa no están conectados, este programa
# hace el papel del nodo: cada opción del menú crea el mismo mensaje que
# enviaría el nodo y lo guarda en la base de datos que lee el tablero.

import sqlite3
import os

print("SENDER DB:")
print(os.path.abspath("neighbornet.db"))

DB = "neighbornet.db"

while True:
    print("\n========================")
    print(" NeighborNet Node ")
    print("========================")
    print("1 - Request Water")
    print("2 - Request Food")
    print("3 - Request Medicine")
    print("4 - Send Flood Alert")
    print("5 - Add Available Resources")
    print("6 - Create Delivery")
    print("7 - Exit")

    choice = input("\nSelect Option: ")

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    # --------------------
    # WATER REQUEST
    # --------------------
    if choice == "1":
        house = input("House Name: ")
        cursor.execute(
            """
            INSERT INTO requests
            (house, resource, status)
            VALUES
            (?, ?, ?)
            """,
            (house, "Water", "Pending")
        )
        print("Water request sent.")

    # --------------------
    # FOOD REQUEST
    # --------------------
    elif choice == "2":
        house = input("House Name: ")
        cursor.execute(
            """
            INSERT INTO requests
            (house, resource, status)
            VALUES
            (?, ?, ?)
            """,
            (house, "Food", "Pending")
        )
        print("Food request sent.")

    # --------------------
    # MEDICINE REQUEST
    # --------------------
    elif choice == "3":
        house = input("House Name: ")
        cursor.execute(
            """
            INSERT INTO requests
            (house, resource, status)
            VALUES
            (?, ?, ?)
            """,
            (house, "Medicine", "Pending")
        )
        print("Medicine request sent.")

    # --------------------
    # FLOOD ALERT
    # --------------------
    elif choice == "4":
        house = input("House Name: ")
        cursor.execute(
            """
            INSERT INTO alerts
            (house, event)
            VALUES
            (?, ?)
            """,
            (house, "Flood Detected")
        )
        print("Flood alert created.")

    # --------------------
    # AVAILABLE RESOURCE
    # --------------------
    elif choice == "5":
        house = input("House Name: ")
        water = int(input("Water Available: "))
        food = int(input("Food Available: "))
        medicine = int(input("Medicine Available (0/1): "))
        cursor.execute(
            """
            INSERT INTO resources
            (house, water, food, medicine)
            VALUES
            (?, ?, ?, ?)
            """,
            (house, water, food, medicine)
        )
        print("Resource inventory added.")

    # --------------------
    # DELIVERY
    # --------------------
    elif choice == "6":
        resource = input("Resource: ")
        from_house = input("From House: ")
        to_house = input("To House: ")
        volunteer = input("Volunteer Name: ")
        cursor.execute(
            """
            INSERT INTO deliveries
            (resource, from_house, to_house, volunteer, status)
            VALUES
            (?, ?, ?, ?, ?)
            """,
            (resource, from_house, to_house, volunteer, "In Transit")
        )
        print("Delivery created.")

    # --------------------
    # EXIT
    # --------------------
    elif choice == "7":
        conn.close()
        print("Exiting...")
        break

    else:
        print("Invalid Option")

    conn.commit()
    conn.close()
