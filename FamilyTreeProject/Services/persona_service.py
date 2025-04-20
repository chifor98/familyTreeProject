# c:\Users\Chifor\FamilyTreeProject\FamilyTreeProject\Services\persona_service.py
import reflex as rx
from ..Models.persona_model import Personas # Importa tu modelo REAL
import sqlmodel # Necesario para la sesión

def select_all_personas_service() -> list[Personas]:
    """Obtiene todas las personas de la base de datos."""
    print("[DEBUG Service] Intentando obtener todas las personas...")
    try:
        # rx.session() te da la sesión de SQLAlchemy configurada por Reflex
        with rx.session() as session:
            # Usa sqlmodel o SQLAlchemy para la consulta
            statement = sqlmodel.select(Personas)
            results = session.exec(statement).all()

            # ¡DEBUG CLAVE! Imprime los resultados CRUDOS obtenidos
            print(f"[DEBUG Service] Resultados de la DB (objetos Personas): {results}")

            # results ya debería ser una lista de objetos Personas si el modelo está bien definido
            return results # Devuelve la lista de objetos
    except Exception as e:
        # Imprime cualquier error que ocurra durante la consulta
        print(f"[ERROR Service] Error al obtener personas: {e}")
        import traceback
        traceback.print_exc() # Imprime el stack trace completo del error
        return [] # Devuelve una lista vacía en caso de error
