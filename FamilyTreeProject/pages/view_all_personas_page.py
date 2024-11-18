import reflex as rx
from ..Models.persona_model import Personas
from ..Services.persona_service import select_all_personas_service

class PersonaState(rx.State):
    personas: list[Personas]
    
    @rx.background
    async def get_all_personas(self):
        print("[DEBUG] Iniciando carga de personas...")
        async with self:
            print("[DEBUG] Obteniendo todas las personas del servicio...")
            self.personas = select_all_personas_service()
            print(f"[DEBUG] Personas cargadas: {self.personas}")
    
@rx.page(route='/personas', title='Personas', on_load=PersonaState.get_all_personas)
def personas_page() -> rx.Component:
    print("[DEBUG] Renderizando página 'personas'")
    print(f"[DEBUG] Estado actual de PersonaState.personas: {PersonaState.personas}")
    return rx.flex(
        rx.heading('Personas', align='center'),
        table_personas(PersonaState.personas),
        direction='column',
        style={"width": "60vw", "margin": "auto"}
    )
    
def table_personas(list_personas: list[Personas]) -> rx.Component: 
    print("[DEBUG] Construyendo tabla de personas...")
    print(f"[DEBUG] Lista de personas recibida: {list_personas}")
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
            rx.foreach(list_personas, row_table)
        )
    )
    
def row_table(persona: Personas) -> rx.Component:
    print("[DEBUG] Creando fila para persona...")
    print(f"[DEBUG] Datos de la persona: {persona}")
    return rx.table.row(
        rx.table.cell(persona.nombre),
        rx.table.cell(persona.apellidos),
        rx.table.cell(persona.email),
        rx.table.cell(persona.usuario),
        rx.table.cell(rx.hstack(
            rx.button('Eliminar')
        ))
    )
