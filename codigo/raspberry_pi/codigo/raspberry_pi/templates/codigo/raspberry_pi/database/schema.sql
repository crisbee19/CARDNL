-- Estructura de la base de datos neighbornet.db
-- Las columnas created_at y timestamp aparecen en la base de datos de la
-- Raspberry Pi (DB Browser); confirmar que coinciden con la versión final.

CREATE TABLE IF NOT EXISTS requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    house TEXT,
    resource TEXT,
    status TEXT,
    created_at TEXT
);

CREATE TABLE IF NOT EXISTS resources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    house TEXT,
    water INTEGER,
    food INTEGER,
    medicine INTEGER
);

CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    house TEXT,
    event TEXT,
    timestamp TEXT
);

CREATE TABLE IF NOT EXISTS deliveries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    resource TEXT,
    from_house TEXT,
    to_house TEXT,
    volunteer TEXT,
    status TEXT
);
