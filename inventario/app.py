from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = 'inventario.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    with app.app_context():
        db = get_db()
        db.execute('''CREATE TABLE IF NOT EXISTS inventario
                      (producto_id INTEGER PRIMARY KEY, cantidad INTEGER)''')
        db.commit()

@app.route('/inventario/<int:producto_id>', methods=['GET'])
def obtener_inventario(producto_id):
    db = get_db()
    cur = db.execute("SELECT cantidad FROM inventario WHERE producto_id = ?", (producto_id,))
    resultado = cur.fetchone()
    
    if resultado:
        return jsonify({"producto_id": producto_id, "cantidad": resultado['cantidad']}), 200
    else:
        return jsonify({"mensaje": "Producto no encontrado"}), 404

if __name__ == '__main__':
    init_db()
    app.run(port=5001)