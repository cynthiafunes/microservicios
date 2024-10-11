import sqlite3
from flask import Flask

DATABASE = 'inventario.db'

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
