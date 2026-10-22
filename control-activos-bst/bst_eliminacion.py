from typing import Optional, Tuple
from nodo import Nodo

class EliminacionMixin:

    def eliminar(self, codigo: int) -> bool:
        if isinstance(codigo, bool) or not isinstance(codigo, int):
            raise TypeError("El codigo patrimonial debe ser un numero entero.")
        if codigo <= 0:
            raise ValueError("El codigo patrimonial debe ser mayor que cero.")

        self.raiz, eliminado = self._eliminar_recursivamente(self.raiz, codigo)
        return eliminado

    def _eliminar_recursivamente(self, nodo: Optional[Nodo], codigo: int) -> Tuple[Optional[Nodo], bool]:
        if nodo is None:
            return None, False
        clave_nodo = nodo.equipo.codigo_patrimonial

        if codigo < clave_nodo:
            nodo.izquierdo, eliminado = self._eliminar_recursivamente(nodo.izquierdo, codigo)
            return nodo, eliminado

        if codigo > clave_nodo:
            nodo.derecho, eliminado = self._eliminar_recursivamente(nodo.derecho, codigo)
            return nodo, eliminado

        # Sin hijo izquierdo: devuelve el derecho, o None si era una hoja.
        if nodo.izquierdo is None:
            return nodo.derecho, True

        if nodo.derecho is None:
            return nodo.izquierdo, True

        # Dos hijos: trasladar el Equipo completo y quitar el nodo del sucesor.
        sucesor = self._minimo_eliminacion(nodo.derecho)
        nodo.equipo = sucesor.equipo
        nodo.derecho, _ = self._eliminar_recursivamente(nodo.derecho, sucesor.equipo.codigo_patrimonial)
        return nodo, True

    def _minimo_eliminacion(self, nodo: Nodo) -> Nodo:
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual


