from typing import List, Optional
from nodo import Nodo

class EstadisticasMixin:
    def contar_nodos(self) -> int:
        return self._contar_nodos_recursivamente(self.raiz)

    def _contar_nodos_recursivamente(self, nodo: Optional[Nodo]) -> int:
        # Caso base: rama vacía, aporta 0 nodos.
        if nodo is None:
            return 0

        # Caso recursivo: nodo actual (1) + los de cada lado.
        return (1
                + self._contar_nodos_recursivamente(nodo.izquierdo)
                + self._contar_nodos_recursivamente(nodo.derecho))

    def contar_hojas(self) -> int:
        return self._contar_hojas_recursivamente(self.raiz)

    def _contar_hojas_recursivamente(self, nodo: Optional[Nodo]) -> int:
        # Caso base 1: rama vacía, no hay hojas.
        if nodo is None:
            return 0
        # Caso base 2: nodo sin hijos, es una hoja.
        if nodo.izquierdo is None and nodo.derecho is None:
            return 1

        # Caso recursivo: hojas de cada lado.
        return (self._contar_hojas_recursivamente(nodo.izquierdo)
                + self._contar_hojas_recursivamente(nodo.derecho))

    def altura(self) -> int:
        return self._altura_recursivamente(self.raiz)

    def _altura_recursivamente(self, nodo: Optional[Nodo]) -> int:
        # Caso base: árbol vacío = -1, así una hoja da 0.
        if nodo is None:
            return -1

        # Caso recursivo: 1 arista + el lado más profundo.
        altura_izquierda = self._altura_recursivamente(nodo.izquierdo)
        altura_derecha = self._altura_recursivamente(nodo.derecho)
        return 1 + max(altura_izquierda, altura_derecha)

    def validar_bst(self) -> bool:
        return self._validar_recursivamente(self.raiz, None, None)

    def _validar_recursivamente(self, nodo: Optional[Nodo], minimo: Optional[int], maximo: Optional[int]) -> bool:
        # Caso base: rama vacía, no rompe nada.
        if nodo is None:
            return True

        # Caso recursivo: primero se revisa este nodo contra los límites...
        codigo = nodo.equipo.codigo_patrimonial
        if minimo is not None and codigo <= minimo:
            return False
        if maximo is not None and codigo >= maximo:
            return False

        return (self._validar_recursivamente(nodo.izquierdo, minimo, codigo)
                and self._validar_recursivamente(nodo.derecho, codigo, maximo))

    def visualizar(self) -> str:
        lineas: List[str] = []
        self._visualizar_recursivamente(self.raiz, 0, "raiz", lineas)
        if not lineas:
            return "El arbol esta vacio."
        return "\n".join(lineas)

    def _visualizar_recursivamente(self, nodo: Optional[Nodo], nivel: int, lado: str, lineas: List[str]) -> None:
        # Caso base: rama vacía, no hay nada que mostrar.
        if nodo is None:
            return

        # Caso recursivo: es un preorder que lleva el nivel (profundidad).
        equipo = nodo.equipo
        lineas.append("    " * nivel
                      + f"[{lado}] {equipo.codigo_patrimonial} - {equipo.descripcion}")
        self._visualizar_recursivamente(nodo.izquierdo, nivel + 1, "izq", lineas)
        self._visualizar_recursivamente(nodo.derecho, nivel + 1, "der", lineas)
