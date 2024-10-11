from flask import Flask, request, jsonify
from db_utils import get_db, init_db  # Importa las funciones comunes

app = Flask(__name__)

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
    init_db(app)  # Llama a la función init_db desde db_utils
    app.run(port=5001)
