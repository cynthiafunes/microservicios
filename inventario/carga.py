import sqlite3  # Asegúrate de que esta línea esté presente
from db_utils import get_db  # Importa get_db para reutilizarla

def agregar_articulo(producto_id, cantidad):
    db = get_db()
    try:
        db.execute("INSERT INTO inventario (producto_id, cantidad) VALUES (?, ?)", (producto_id, cantidad))
        db.commit()
        print(f"Artículo {producto_id} agregado con cantidad {cantidad}")
    except sqlite3.IntegrityError:
        print(f"Error: el artículo con producto_id {producto_id} ya existe.")
    finally:
        db.close()

if __name__ == '__main__':
    producto_id = int(input("Introduce el ID del producto: "))
    cantidad = int(input("Introduce la cantidad del producto: "))
    
    agregar_articulo(producto_id, cantidad)
