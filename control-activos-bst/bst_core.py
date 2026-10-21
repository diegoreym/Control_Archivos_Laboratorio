from typing import List, Optional
from equipo import Equipo
from nodo import Nodo

class BSTCore:
    def __init__(self) -> None:
        self.raiz: Optional[Nodo] = None
        self.ultima_traza: List[str] = []
        self.nodos_examinados: int = 0

    # ------------------------------------------------------------------
    # Auxiliares de traza
    # ------------------------------------------------------------------
    def _iniciar_traza(self) -> None:
        self.ultima_traza = []
        self.nodos_examinados = 0

    def _registrar(self, mensaje: str, mostrar: bool) -> None:
        self.ultima_traza.append(mensaje)
        if mostrar:
            print(mensaje)

    # ------------------------------------------------------------------
    # Operaciones públicas
    # ------------------------------------------------------------------
    def esta_vacio(self) -> bool:
        return self.raiz is None

    def insertar(self, equipo: Equipo, traza: bool = False) -> bool:
        """Inserta un equipo ordenado por código patrimonial"""
        if not isinstance(equipo, Equipo):
            raise TypeError("Solo se pueden insertar objetos de tipo Equipo.")

        self._iniciar_traza()
        codigo = equipo.codigo_patrimonial

        if self.raiz is None:
            self.raiz = Nodo(equipo)
            self._registrar(f"Árbol vacío: {codigo} se inserta como raíz.", traza)
            return True

        actual = self.raiz
        while True:
            clave = actual.equipo.codigo_patrimonial
            self.nodos_examinados += 1

            if codigo == clave:
                self._registrar(
                    f"Comparar {codigo} con {clave}: iguales -> duplicado, "
                    "se rechaza.",
                    traza,
                )
                return False

            if codigo < clave:
                if actual.izquierdo is None:
                    actual.izquierdo = Nodo(equipo)
                    self._registrar(
                        f"Comparar {codigo} con {clave}: menor -> izquierda libre, "
                        f"se inserta {codigo}.",
                        traza,
                    )
                    return True
                self._registrar(
                    f"Comparar {codigo} con {clave}: menor -> ir a la izquierda.",
                    traza,
                )
                actual = actual.izquierdo
            else:
                if actual.derecho is None:
                    actual.derecho = Nodo(equipo)
                    self._registrar(
                        f"Comparar {codigo} con {clave}: mayor -> derecha libre, "
                        f"se inserta {codigo}.",
                        traza,
                    )
                    return True
                self._registrar(
                    f"Comparar {codigo} con {clave}: mayor -> ir a la derecha.",
                    traza,
                )
                actual = actual.derecho

    def buscar(self, codigo: int, traza: bool = False) -> Optional[Equipo]:
        """Busca un equipo por código patrimonial."""
        
        if isinstance(codigo, bool) or not isinstance(codigo, int):
            raise TypeError("El código patrimonial debe ser un número entero.")

        self._iniciar_traza()

        if self.raiz is None:
            self._registrar("Árbol vacío: no hay nada que buscar.", traza)
            return None

        actual = self.raiz
        while actual is not None:
            clave = actual.equipo.codigo_patrimonial
            self.nodos_examinados += 1

            if codigo == clave:
                self._registrar(
                    f"Comparar {codigo} con {clave}: iguales -> encontrado.", traza
                )
                return actual.equipo

            if codigo < clave:
                self._registrar(
                    f"Comparar {codigo} con {clave}: menor -> ir a la izquierda.",
                    traza,
                )
                actual = actual.izquierdo
            else:
                self._registrar(
                    f"Comparar {codigo} con {clave}: mayor -> ir a la derecha.",
                    traza,
                )
                actual = actual.derecho

        self._registrar(f"Se llegó a una rama vacía: {codigo} no existe.", traza)
        return None
