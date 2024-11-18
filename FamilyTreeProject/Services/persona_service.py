from ..Repository.persona_repository import select_all

def select_all_personas_service():
    users = select_all()
    print(users)
    return users