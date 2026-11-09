-- Datos de prueba usados para llenar el tablero

INSERT INTO requests (house, resource, status) VALUES ('House C', 'Food', 'Pending');
INSERT INTO requests (house, resource, status) VALUES ('House D', 'Medicine', 'Pending');

INSERT INTO resources (house, water, food, medicine) VALUES ('House B', 10, 20, 1);
INSERT INTO resources (house, water, food, medicine) VALUES ('House E', 4, 8, 0);
INSERT INTO resources (house, water, food, medicine) VALUES ('Community Center', 25, 40, 1);

INSERT INTO alerts (house, event) VALUES ('House A', 'Flood Detected');
INSERT INTO alerts (house, event) VALUES ('House F', 'Power Outage');

INSERT INTO deliveries (resource, from_house, to_house, volunteer, status)
VALUES ('Water', 'House B', 'House A', 'Juan', 'In Transit');
INSERT INTO deliveries (resource, from_house, to_house, volunteer, status)
VALUES ('Food', 'Community Center', 'House C', 'Maria', 'Delivered');
