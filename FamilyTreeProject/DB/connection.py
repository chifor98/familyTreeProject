from sqlmodel import create_engine
from sqlalchemy.exc import OperationalError, ArgumentError # Importar excepciones específicas es útil
import sys # Para poder salir si la conexión falla

def connect():
    """Crea y retorna un engine de SQLModel para la base de datos."""
    # Corrige el URI de conexión usando ":" para separar usuario y contraseña
    # Asegúrate que pymysql está instalado: pip install pymysql
    connection_string = "mysql+pymysql://root:admin@localhost:3306/familytree"
    try:
        engine = create_engine(connection_string)
        print(f"Intentando conectar a: {connection_string}")
        # --- Aquí está la prueba ---
        # Intentamos establecer una conexión real.
        # Usamos 'with' para asegurarnos de que la conexión se cierre automáticamente.
        with engine.connect() as connection:
            print("¡Conexión exitosa a la base de datos!")
        # --------------------------
        return engine
    except ArgumentError as arg_err:
        print(f"Error en los argumentos de la cadena de conexión: {arg_err}")
        print(f"Verifica la sintaxis de: {connection_string}")
        return None # O podrías lanzar la excepción: raise
    except OperationalError as op_err:
        # Esta excepción es común para problemas como:
        # - Base de datos no existe
        # - Servidor no accesible (apagado, firewall)
        # - Credenciales incorrectas (usuario/contraseña)
        # - Driver pymysql no instalado
        print(f"Error al intentar conectar a la base de datos: {op_err}")
        print("Posibles causas:")
        print("- ¿Está el servidor MySQL en ejecución en localhost:3306?")
        print("- ¿Son correctas las credenciales (root/admin)?")
        print("- ¿Existe la base de datos 'familytree'?")
        print("- ¿Está instalado el driver 'pymysql' (pip install pymysql)?")
        print("- ¿Hay algún firewall bloqueando la conexión?")
        return None # O podrías lanzar la excepción: raise
    except Exception as e:
        # Captura cualquier otro error inesperado
        print(f"Ocurrió un error inesperado al conectar: {e}")
        return None # O podrías lanzar la excepción: raise

# --- Código para probar la función connect ---
if __name__ == "__main__":
    print("Probando la conexión a la base de datos...")
    db_engine = connect()

    if db_engine:
        print("La función connect() retornó un engine válido.")
        # Aquí podrías continuar usando el engine si la conexión fue exitosa
        # Por ejemplo:
        # with Session(db_engine) as session:
        #    # hacer algo con la sesión
        #    pass
    else:
        print("La función connect() falló al establecer la conexión.")
        # Podrías decidir terminar el script si la conexión es esencial
        # sys.exit(1)