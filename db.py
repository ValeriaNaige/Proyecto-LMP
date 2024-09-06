from sqlalchemy import create_engine, text

engine = create_engine('mssql+pyodbc://@DESKTOP-A5IL2RD\\SQLEXPRESS/agenda?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')


def getEvents():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * From contactos"))
        contacts_list = [row for row in result]
        return contacts_list
    
def insert_event(nombre, telefono):
    try:
        with engine.connect() as connection:
            query = text("INSERT INTO contactos (nombre, telefono) VALUES (:nombre, :telefono)")
            connection.execute(query, {"nombre": nombre, "telefono": telefono})
            connection.commit()
            print("Insert realizado datos ", nombre, telefono)
            connection.close()
    except Exception as e:
        print(f"Error al insertar evento: {e}")

def delete_event(id):
    try:
        with engine.connect() as connection:
            query = text("DELETE FROM contactos WHERE id = (:id)")
            connection.execute(query, {"id":id})
            connection.commit()
            print("Delete realizado")
            connection.close()
    except Exception as e:
        print(f"Error al eliminar evento: {e}")

def edit_event(id, nombre, telefono):
    try:
        with engine.connect() as connection:
            query = text("UPDATE contactos SET nombre = (:nombre), telefono = (:telefono) WHERE id = (:id)")
            connection.execute(query, {"nombre": nombre, "telefono": telefono, "id":id})
            connection.commit()
            print("Update realizado")
            connection.close()
    except Exception as e:
        print(f"Error al editar evento: {e}")