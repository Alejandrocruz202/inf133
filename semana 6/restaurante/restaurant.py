import sqlite3

conn =sqlite3.connect("restaurant.db")

conn.execute(
    """
    CREATE TABLE PLATOS
    (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio INTEGER NOT NULL,
        categoria TEXT NOT NULL   
    );
    """
)
conn.execute(
    """
    CREATE TABLE PLATOS
    (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio INTEGER NOT NULL,
        categoria TEXT NOT NULL   
    );
    """
)
conn.execute(
    """
    CREATE TABLE MESAS
    (
        id INTEGER PRIMARY KEY,
        numero INTEGER NOT NULL,  
    );
    """
)
conn.execute(
    """
    CREATE TABLE PEDIDOS
    (
        id INTEGER PRIMARY KEY,
        plato_id INTEGER NOT NULL,
        mesa_id INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        fecha NOT NULL   
    );
    """
)