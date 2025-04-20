# c:\Users\Chifor\FamilyTreeProject\FamilyTreeProject\Services\__init__.py
"""
Inicializador del paquete Services.
Expone las funciones de servicio principales.
"""
try:
    # Asume que tienes Services/persona_service.py
    from .persona_service import select_all_personas_service
    # Importa otras funciones de servicio aquí si las tienes
    # from .persona_service import add_persona_service, delete_persona_service

    # Define qué se importa con 'from .Services import *'
    # y sirve como documentación de la interfaz pública.
    __all__ = [
        'select_all_personas_service',
        # Añade otros nombres de funciones de servicio aquí
        # 'add_persona_service', 'delete_persona_service',
    ]
except ImportError:
    print("ADVERTENCIA: No se pudo importar desde Services.persona_service.")
    __all__ = [] # Deja __all__ vacío si la importación falla
