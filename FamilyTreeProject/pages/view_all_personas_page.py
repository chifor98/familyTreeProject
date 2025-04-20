# c:\Users\Chifor\FamilyTreeProject\FamilyTreeProject\pages\view_all_personas_page.py
import reflex as rx
from ..Models.persona_model import Personas
from ..Services.persona_service import select_all_personas_service
# Make sure select_all_personas_service is correctly imported and defined

class PersonaState(rx.State):
    # Initialize with an empty list
    personas: list[Personas] = []

    # If select_all_personas_service is SYNCHRONOUS (most likely case):
    def get_all_personas(self):
        print("[DEBUG] Iniciando carga de personas (on_load)...")
        print("[DEBUG] Obteniendo todas las personas del servicio...")
        # Directly assign the result - NO 'async with self:' here
        personas_data = select_all_personas_service()
        print(f"[DEBUG] Personas obtenidas del servicio: {personas_data}")
        self.personas = personas_data
        print(f"[DEBUG] Estado personas actualizado: {self.personas}")

    # --- OR ---

    # If select_all_personas_service is ASYNCHRONOUS (uses async def):
    # async def get_all_personas(self):
    #     print("[DEBUG] Iniciando carga de personas (on_load)...")
    #     print("[DEBUG] Obteniendo todas las personas del servicio (async)...")
    #     # Use await if the service function is async
    #     personas_data = await select_all_personas_service()
    #     print(f"[DEBUG] Personas obtenidas del servicio: {personas_data}")
    #     # Directly assign the result - NO 'async with self:' here
    #     self.personas = personas_data
    #     print(f"[DEBUG] Estado personas actualizado: {self.personas}")


@rx.page(route='/personas', title='Personas', on_load=PersonaState.get_all_personas)
def personas_page() -> rx.Component:
    print("[DEBUG] Renderizando página 'personas'")
    # It's safer to access the state variable via the state class itself
    # in the render function, especially if on_load might not have finished
    # immediately (though Reflex usually handles this).
    # Using PersonaState.personas directly is fine here.
    print(f"[DEBUG] Estado actual de PersonaState.personas para renderizar: {PersonaState.personas}")
    return rx.flex(
        rx.heading('Personas', align='center'),
        # Pass the state variable to the table function
        table_personas(PersonaState.personas),
        direction='column',
        style={"width": "60vw", "margin": "auto"}
    )

def table_personas(list_personas: list[Personas]) -> rx.Component:
    print("[DEBUG] Construyendo tabla de personas...")
    # Check if list_personas is None or not iterable before passing to rx.foreach
    # Although initializing in the state should prevent None.
    if list_personas is None:
        print("[DEBUG] list_personas es None, devolviendo tabla vacía.")
        list_personas = [] # Ensure it's an empty list if None

    print(f"[DEBUG] Lista de personas recibida para tabla: {list_personas}")
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell('Nombre'),
                rx.table.column_header_cell('Apellidos'),
                rx.table.column_header_cell('Email'),
                rx.table.column_header_cell('Usuario'),
                rx.table.column_header_cell('Acción'),
            )
        ),
        rx.table.body(
            # rx.foreach iterates over the list_personas state variable
            rx.foreach(list_personas, row_table)
        )
    )

def row_table(persona: Personas) -> rx.Component:
    # This function receives individual persona objects from rx.foreach
    print(f"[DEBUG] Creando fila para persona: {persona}")
    # Ensure persona object has the expected attributes
    return rx.table.row(
        rx.table.cell(getattr(persona, 'nombre', 'N/A')), # Use getattr for safety
        rx.table.cell(getattr(persona, 'apellidos', 'N/A')),
        rx.table.cell(getattr(persona, 'email', 'N/A')),
        rx.table.cell(getattr(persona, 'usuario', 'N/A')),
        rx.table.cell(rx.hstack(
            # Add on_click handler later if needed
            rx.button('Eliminar')
        ))
    )

