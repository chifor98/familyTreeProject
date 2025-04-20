# c:\Users\Chifor\FamilyTreeProject\FamilyTreeProject\navigation\__init__.py
"""
Inicializador del paquete navigation.
Expone el estado de navegación y las rutas.
"""
from .state import NavState
from . import routes # Permite hacer navigation.routes.HOME_ROUTE etc.

# Opcional: Exponer rutas individuales si se usan muy frecuentemente
# from .routes import HOME_ROUTE, ABOUT_US_ROUTE, PERSONAS_LIST_ROUTE

# Define qué se importa con 'from .navigation import *'
# y sirve como documentación de la interfaz pública.
__all__ = [
    'NavState',
    'routes',
    # Añadir aquí las rutas específicas si se importaron arriba
    # 'HOME_ROUTE', 'ABOUT_US_ROUTE', 'PERSONAS_LIST_ROUTE',
]
