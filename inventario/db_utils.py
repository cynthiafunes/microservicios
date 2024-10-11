import sqlite3
from flask import Flask
import os

# Cambia la ruta a la base de datos dentro de la carpeta del microservicio
DATABASE = os.path.join(os.path.dirname(__file__), 'inventario.db')

def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def init_db(app):
    with app.app_context():
        db = get_db()
        db.execute('''CREATE TABLE IF NOT EXISTS inventario
                      (producto_id INTEGER PRIMARY KEY, cantidad INTEGER)''')
        db.commit()
