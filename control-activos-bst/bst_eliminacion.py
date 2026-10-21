from typing import Optional
from nodo import Nodo


class EliminacionMixin:
    def eliminar(self, codigo: int) -> bool:

        # Validar el tipo de código.
        if isinstance(codigo, bool) or not isinstance(codigo, int):
            raise TypeError(
                "El código patrimonial debe ser un número entero."
            )

        if codigo <= 0:
            raise ValueError(
                "El código patrimonial debe ser mayor que cero."
            )

        # Ejecutar la eliminación desde la raíz.
        self.raiz, eliminado = self._eliminar_recursivamente(
            self.raiz, codigo
        )

        return eliminado

    def _eliminar_recursivamente(
        self, nodo: Optional[Nodo], codigo: int
    ) -> tuple[Optional[Nodo], bool]:
        # sourcery skip: assign-if-exp, hoist-repeated-if-condition, reintroduce-else


        # CASO BASE: ÁRBOL VACÍO O CÓDIGO INEXISTENTE
        if nodo is None:
            return None, False

        codigo_actual = nodo.equipo.codigo_patrimonial

        # BUSCAR EN EL SUBÁRBOL IZQUIERDO
        if codigo < codigo_actual:

            nodo.izquierdo, eliminado = (
                self._eliminar_recursivamente(
                    nodo.izquierdo, codigo
                )
            )

            return nodo, eliminado

        # BUSCAR EN EL SUBÁRBOL DERECHO
        if codigo > codigo_actual:

            nodo.derecho, eliminado = (
                self._eliminar_recursivamente(
                    nodo.derecho, codigo
                )
            )

            return nodo, eliminado

        # Se encontró el nodo que debe eliminarse.


        # CASO 1: EL NODO ES UNA HOJA

        if nodo.izquierdo is None and nodo.derecho is None:
            return None, True

        # CASO 2: EL NODO TIENE UN SOLO HIJO

        if nodo.izquierdo is None:

            return nodo.derecho, True

        if nodo.derecho is None:

            return nodo.izquierdo, True

        # CASO 3: EL NODO TIENE DOS HIJOS
        sucesor = self._minimo(nodo.derecho)

        nodo.equipo = sucesor.equipo

        nodo.derecho, _ = self._eliminar_recursivamente(
            nodo.derecho,
            sucesor.equipo.codigo_patrimonial
        )

        return nodo, True

    def _minimo(self, nodo: Nodo) -> Nodo:

        actual = nodo

        while actual.izquierdo is not None:
            actual = actual.izquierdo

        return actual

