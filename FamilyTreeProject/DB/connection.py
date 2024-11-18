from sqlmodel import create_engine

def connect():
    # Corrige el URI de conexión usando ":" para separar usuario y contraseña
    engine = create_engine("mysql+pymysql://root:admin@localhost:3306/familytree")
    print('Engine encontrado?')
    print(engine)
    return engine
