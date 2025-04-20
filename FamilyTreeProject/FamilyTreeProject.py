# c:\Users\Chifor\FamilyTreeProject\FamilyTreeProject\FamilyTreeProject.py
import reflex as rx
from rxconfig import config
from .ui.navbar import navbar_dropdown
from .ui.base import base_page
#from . import pages # Importa el paquete 'pages'

# --- Importa las páginas específicas que vas a añadir (opcional pero claro) ---
# Esto no es estrictamente necesario si usas pages.nombre_pagina,
# pero puede hacer el código más legible.
from .pages.view_all_personas_page import personas_page
from .pages.about import about_page
from .pages.userRegistration import signup_multiple_thirdparty # Asumiendo que esta es tu página de registro
# from .pages.login import signup_default # Necesitarás decorar y renombrar esta

class State(rx.State):
     """ The app state."""
     label= "Welcome to Reflex!s"

     def handle_title_input_change(self, val):
         self.label = val
     def did_click(self):
         print("Hello world did click")

def index() -> rx.Component:
    # Contenido para la página de inicio
    return base_page(rx.vstack(rx.heading("Bienvenido a Family Tree")))

# --- Crea la instancia de la App ---
app = rx.App()

# --- Añade las páginas ---
app.add_page(index) # Ruta '/' (por defecto para index)

# Para about, es mejor usar la ruta del decorador si está definida
# Descomenta el decorador en about.py y quita route='/about' aquí
# @rx.page(route=routes.ABOUT_US_ROUTE) en about.py
app.add_page(about_page) # Reflex usará la ruta del decorador @rx.page

# Añade la página de personas (usará la ruta '/personas' del decorador)
app.add_page(personas_page) # <-- AÑADE ESTA LÍNEA

# Añade la página de registro (usará la ruta '/register' del decorador)
app.add_page(signup_multiple_thirdparty) # <-- AÑADE ESTA LÍNEA

# Añade la página de login (¡NECESITA DECORADOR Y RENOMBRAR!)
# 1. En login.py, añade: @rx.page(route='/login', title='Login')
# 2. Renombra la función a algo como 'login_page'
# 3. Importa 'login_page' arriba
# 4. Descomenta la siguiente línea:
# app.add_page(login_page) # <-- AÑADE ESTA LÍNEA (después de arreglar login.py)

