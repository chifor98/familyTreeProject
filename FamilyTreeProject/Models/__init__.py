# c:\Users\Chifor\FamilyTreeProject\FamilyTreeProject\Models\__init__.py
"""
Inicializador del paquete Models.
Expone los modelos de datos principales.
"""
from .persona_model import Personas

# Define qué se importa con 'from .Models import *'
# y sirve como documentación de la interfaz pública.
__all__ = ['Personas']
