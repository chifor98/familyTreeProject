import reflex as rx
from typing import Optional
from sqlmodel import Field

class Personas(rx.Model, table=True):
    # id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    apellidos: str
    fechaNacimiento: str
    sexo: str
    padreId: str
    madreId: str
    usuario: str
    email: str
    contrasena: str

    def __str__(self):
        return f"Personas(nombre={self.nombre})"

    def __repr__(self):
        return self.__str__()
