from bst_core import BSTCore
from bst_eliminacion import EliminacionMixin
from bst_recorridos import RecorridosMixin
from bst_estadisticas import EstadisticasMixin


class ArbolBST(
    BSTCore,
    EliminacionMixin,
    RecorridosMixin,
    EstadisticasMixin
):

    def __init__(self) -> None:
        super().__init__()

    def obtener_raiz(self): 
        if self.raiz is None:
            return None

        return self.raiz.equipo

    def __str__(self) -> str:
        if self.esta_vacio():
            return "El árbol binario de búsqueda está vacío."

        return self.visualizar()


if __name__ == "__main__":
    print("Módulo ArbolBST")
    print("Este archivo integra las operaciones del BST.")
    print("Ejecute main.py para utilizar el sistema.")

