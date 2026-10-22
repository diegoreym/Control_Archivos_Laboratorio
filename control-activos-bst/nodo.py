from typing import Optional
from equipo import Equipo

class Nodo:
    def __init__(self, equipo: Equipo) -> None:
        self.equipo: Equipo = equipo
        self.izquierdo: Optional["Nodo"] = None
        self.derecho: Optional["Nodo"] = None

    def __repr__(self) -> str:
        return f"Nodo({self.equipo.codigo_patrimonial})"
