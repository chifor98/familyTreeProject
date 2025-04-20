# c:\Users\Chifor\FamilyTreeProject\FamilyTreeProject\DB\__init__.py
"""
Inicializador del paquete DB.
Expone la función principal de conexión.
"""
from .connection import connect

# Define qué se importa con 'from .DB import *'
# y sirve como documentación de la interfaz pública.
__all__ = ['connect']
