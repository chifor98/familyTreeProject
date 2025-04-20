# c:\Users\Chifor\FamilyTreeProject\FamilyTreeProject\pages\__init__.py
"""
Inicializador del paquete pages.

¡IMPORTANTE! Este archivo debe importar todas las funciones de página
decoradas con @rx.page para asegurar que Reflex las descubra
y registre sus rutas correctamente al iniciar la aplicación.
"""
from .about import about_page
from .view_all_personas_page import personas_page

# Intenta importar otras páginas, asegurándote de que existan,
# tengan el decorador @rx.page y los nombres coincidan.
try:
    # Asume que renombraste la función en userRegistration.py a registration_page
    # y le añadiste @rx.page(route='/register', ...)
    from .userRegistration import registration_page
except ImportError:
    print("ADVERTENCIA: No se pudo importar 'registration_page' desde pages.userRegistration.")
    registration_page = None # Define como None si falla la importación

try:
    # Asume que renombraste la función en login.py a login_page
    # y le añadiste @rx.page(route='/login', ...)
    from .login import login_page
except ImportError:
    print("ADVERTENCIA: No se pudo importar 'login_page' desde pages.login.")
    login_page = None # Define como None si falla la importación


# __all__ define qué se importa con 'from .pages import *' (generalmente no recomendado)
# pero también sirve como documentación de las páginas principales del paquete.
_all_potential_pages = [
    'about_page',
    'personas_page',
    'registration_page',
    'login_page',
]

# Filtra la lista __all__ para incluir solo las páginas que se importaron correctamente.
__all__ = [name for name in _all_potential_pages if globals().get(name) is not None]

# Limpia las variables temporales si es necesario (aunque no es estrictamente requerido)
del _all_potential_pages
