class Equipo:
    """Representa un equipo identificado por un código patrimonial inmutable."""

    CONDICIONES_VALIDAS = ("Operativo", "En mantenimiento", "Inoperativo") # TUPLA INICIALIZADA

    def __init__(self,codigo_patrimonial: int,descripcion: str,laboratorio: str,condicion: str,responsable: str,) -> None:
        self._codigo_patrimonial = self._validar_codigo(codigo_patrimonial)
        self.descripcion = descripcion
        self.laboratorio = laboratorio
        self.condicion = condicion
        self.responsable = responsable

    @staticmethod
    def _validar_codigo(codigo: int) -> int:
        if isinstance(codigo, bool) or not isinstance(codigo, int):
            raise TypeError("El código patrimonial debe ser un número entero.")
        if codigo <= 0:
            raise ValueError("El código patrimonial debe ser mayor que cero.")
        return codigo

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        if not isinstance(valor, str):
            raise TypeError(f"{campo} debe ser texto.")
        valor = valor.strip()
        if not valor:
            raise ValueError(f"{campo} es obligatorio.")
        return valor

    @property
    def codigo_patrimonial(self) -> int:
        """Clave usada para ordenar el BST; se expone como solo lectura."""
        return self._codigo_patrimonial

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor: str) -> None:
        self._descripcion = self._validar_texto(valor, "La descripción")

    @property
    def laboratorio(self) -> str:
        return self._laboratorio

    @laboratorio.setter
    def laboratorio(self, valor: str) -> None:
        self._laboratorio = self._validar_texto(valor, "El laboratorio")

    @property
    def condicion(self) -> str:
        return self._condicion

    @condicion.setter
    def condicion(self, valor: str) -> None:
        condicion = self._validar_texto(valor, "La condición")
        condiciones = {estado.casefold(): estado for estado in self.CONDICIONES_VALIDAS}
        if condicion.casefold() not in condiciones:
            opciones = ", ".join(self.CONDICIONES_VALIDAS)
            raise ValueError(f"Condición inválida. Use una de estas opciones: {opciones}.")
        self._condicion = condiciones[condicion.casefold()]

    @property
    def responsable(self) -> str:
        return self._responsable

    @responsable.setter
    def responsable(self, valor: str) -> None:
        self._responsable = self._validar_texto(valor, "El responsable")

    def __str__(self) -> str:
        return (
            f"Código: {self.codigo_patrimonial} | Descripción: {self.descripcion} | "
            f"Laboratorio: {self.laboratorio} | Condición: {self.condicion} | "
            f"Responsable: {self.responsable}"
        )

    def __repr__(self) -> str:
        return (
            "Equipo("
            f"codigo_patrimonial={self.codigo_patrimonial!r}, "
            f"descripcion={self.descripcion!r}, laboratorio={self.laboratorio!r}, "
            f"condicion={self.condicion!r}, responsable={self.responsable!r})" #!r permite que los valores impresos se muestren en comillas
        )
