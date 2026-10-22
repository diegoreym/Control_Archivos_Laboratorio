from typing import List, Optional
from equipo import Equipo
from nodo import Nodo

class RecorridosMixin:
    """Recorridos en profundidad del BST. Usa el self.raiz de BSTCore."""

    def preorder(self) -> List[Equipo]:
        resultado: List[Equipo] = []
        self._preorder(self.raiz, resultado)
        return resultado

    def _preorder(self, nodo: Optional[Nodo], resultado: List[Equipo]) -> None:
        # Caso base: rama vacía, no hay nada que visitar.
        if nodo is None:
            return

        # Caso recursivo
        resultado.append(nodo.equipo)               # 1) el nodo primero
        self._preorder(nodo.izquierdo, resultado)   # 2) subárbol izquierdo
        self._preorder(nodo.derecho, resultado)     # 3) subárbol derecho

    def inorder(self) -> List[Equipo]:
        resultado: List[Equipo] = []
        self._inorder(self.raiz, resultado)
        return resultado

    def _inorder(self, nodo: Optional[Nodo], resultado: List[Equipo]) -> None:
        # Caso base
        if nodo is None:
            return

        # Caso recursivo
        self._inorder(nodo.izquierdo, resultado)    # 1) subárbol izquierdo
        resultado.append(nodo.equipo)               # 2) el nodo en medio
        self._inorder(nodo.derecho, resultado)      # 3) subárbol derecho

    def postorder(self) -> List[Equipo]:
        resultado: List[Equipo] = []
        self._postorder(self.raiz, resultado)
        return resultado

    def _postorder(self, nodo: Optional[Nodo], resultado: List[Equipo]) -> None:
        # Caso base
        if nodo is None:
            return

        # Caso recursivo
        self._postorder(nodo.izquierdo, resultado)  # 1) subárbol izquierdo
        self._postorder(nodo.derecho, resultado)    # 2) subárbol derecho
        resultado.append(nodo.equipo)               # 3) el nodo al final
