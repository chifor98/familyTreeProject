from ..Models.persona_model import Personas
from ..DB.connection import connect
from sqlmodel import Session, select

def select_all():
    engine = connect()
    with Session(engine) as session:
        query = select(Personas)
        print('query')
        print(query)
        return session.exec(query).all()