# c:\Users\Chifor\FamilyTreeProject\FamilyTreeProject\ui\navbar.py
import reflex as rx
# --- Importa las rutas ---
from ..navigation import routes # Importa tus constantes de ruta
from ..navigation.state import NavState # Importa tu NavState modificado

# Helper para crear enlaces del navbar
def navbar_link(text: str, url: str) -> rx.Component:
    """Crea un enlace estilizado para el navbar."""
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

# Componente principal del Navbar
def navbar_dropdown() -> rx.Component:
    """Renderiza el navbar con vistas para escritorio y móvil."""
    # --- Define la ruta de Login ---
    # Asegúrate de que LOGIN_ROUTE esté definido en navigation/routes.py
    # Ejemplo: LOGIN_ROUTE = "/login"
    # Y que tengas una página en pages/login.py con @rx.page(route=routes.LOGIN_ROUTE)
    login_route = getattr(routes, 'LOGIN_ROUTE', '/login') # Usa '/login' como fallback si no está definido

    return rx.box(
        # --- Vista de Escritorio ---
        rx.desktop_only(
            rx.hstack(
                # Logo y Título (enlazado a Home)
                rx.hstack(
                    rx.image(
                        src="/assets/logo.jpg", # Verifica que esta ruta sea correcta
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.link(
                        rx.heading(
                            "Family Tree", size="7", weight="bold" # Cambiado "Reflex" por "Family Tree"
                        ),
                        href=routes.HOME_ROUTE,
                    ),
                    align_items="center",
                ),
                # Enlaces de Navegación
                rx.hstack(
                    navbar_link("Home", routes.HOME_ROUTE),
                    navbar_link("About", routes.ABOUT_US_ROUTE),
                    navbar_link("Personas", routes.PERSONAS_LIST_ROUTE), # Enlace añadido
                    navbar_link("Register", routes.REGISTER_LIST_ROUTE), # Enlace a tu página de registro
                    navbar_link("Log in", login_route), # Enlace a tu página de login
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
                id='my-navbar-hstack-desktop'
            ),
        ),
        # --- Vista Móvil y Tablet ---
        rx.mobile_and_tablet(
            rx.hstack(
                # Logo y Título (no enlazado aquí, solo visual)
                rx.hstack(
                    rx.image(
                        src="/assets/logo.jpg", # Verifica ruta
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Family Tree", size="6", weight="bold" # Cambiado "Reflex" por "Family Tree"
                    ),
                    align_items="center",
                ),
                # Menú desplegable
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30) # Icono de hamburguesa
                    ),
                    rx.menu.content(
                        # --- Items del Menú Móvil ---
                        # Asegúrate de que estos métodos existan en NavState
                        # y que redirijan a las rutas correctas de 'routes.py'
                        rx.menu.item("Home", on_click=NavState.to_home),
                        rx.menu.item("About", on_click=NavState.to_about_us),
                        rx.menu.item("Personas", on_click=NavState.to_personas), # Item añadido
                        # Necesitarás métodos como to_register_page y to_login_page en NavState
                        # que redirijan a routes.REGISTER_LIST_ROUTE y login_route respectivamente.
                        rx.menu.item("Register", on_click=getattr(NavState, 'to_register_page', lambda: rx.redirect(routes.REGISTER_LIST_ROUTE))),
                        rx.menu.item("Login", on_click=getattr(NavState, 'to_login_page', lambda: rx.redirect(login_route))),
                        # Descomenta si tienes estas páginas y métodos en NavState
                        # rx.menu.item("Pricing", on_click=NavState.to_pricing),
                        # rx.menu.item("Contact", on_click=NavState.to_contact),
                    ),
                    justify="end", # Alinea el contenido del menú
                ),
                justify="between", # Espacio entre logo/título y menú
                align_items="center",
            ),
        ),
        # Estilos comunes del Navbar
        bg=rx.color("accent", 3), # Color de fondo
        padding="1em", # Relleno
        width="100%", # Ancho completo
        # Descomenta si quieres que el navbar sea fijo en la parte superior
        # position="fixed",
        # top="0px",
        # z_index="5",
        id="my-main-nav", # ID para posible CSS personalizado
    )

