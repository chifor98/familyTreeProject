# c:\Users\Chifor\FamilyTreeProject\FamilyTreeProject\ui\__init__.py
"""
Inicializador del paquete ui.
Expone los componentes de UI reutilizables principales.
"""
from .base import base_page
from .navbar import navbar_dropdown

# Define qué se importa con 'from .ui import *'
# y sirve como documentación de la interfaz pública.
__all__ = ['base_page', 'navbar_dropdown']
