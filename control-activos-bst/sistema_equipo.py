from arbol_bst import ArbolBST
from equipo import Equipo


class SistemaEquipo:

    def __init__(self) -> None:

        self.arbol = ArbolBST()
        self.modo_demostracion = False


    # MÉTODOS AUXILIARES

    @staticmethod
    def mostrar_encabezado(titulo: str) -> None:
        print("\n" + "=" * 60)
        print(titulo.center(60))
        print("=" * 60)

    @staticmethod
    def pausar() -> None:
        input("\nPresione ENTER para continuar...")

    @staticmethod
    def leer_codigo(mensaje: str) -> int:
        while True:
            entrada = input(mensaje).strip()

            try:
                codigo = int(entrada)

                if codigo <= 0:
                    print(
                        "ERROR: El código patrimonial "
                        "debe ser mayor que cero."
                    )
                    continue

                return codigo

            except ValueError:
                print(
                    "ERROR: Debe ingresar un "
                    "número entero válido."
                )

    @staticmethod
    def leer_texto(mensaje: str) -> str:
        while True:
            texto = input(mensaje).strip()

            if texto:
                return texto

            print("ERROR: Este campo es obligatorio.")

    @staticmethod
    def leer_condicion() -> str:
        condiciones = Equipo.CONDICIONES_VALIDAS

        while True:
            print("\nCondiciones disponibles:")

            for indice, condicion in enumerate(condiciones, 1):
                print(f"{indice}. {condicion}")

            opcion = input("Seleccione una condición: ").strip()

            if opcion.isdigit():
                numero = int(opcion)

                if 1 <= numero <= len(condiciones):
                    return condiciones[numero - 1]

            print("ERROR: Seleccione una condición válida.")

    @staticmethod
    def mostrar_datos_equipo(equipo: Equipo) -> None:
        print("-" * 60)
        print(f"Código patrimonial : {equipo.codigo_patrimonial}")
        print(f"Descripción        : {equipo.descripcion}")
        print(f"Laboratorio        : {equipo.laboratorio}")
        print(f"Condición          : {equipo.condicion}")
        print(f"Responsable        : {equipo.responsable}")
        print("-" * 60)

    def solicitar_datos_equipo(self) -> Equipo:
        codigo = self.leer_codigo(
            "Código patrimonial: "
        )

        descripcion = self.leer_texto(
            "Descripción del equipo: "
        )

        laboratorio = self.leer_texto(
            "Laboratorio: "
        )

        condicion = self.leer_condicion()

        responsable = self.leer_texto(
            "Responsable: "
        )

        return Equipo(
            codigo_patrimonial=codigo,
            descripcion=descripcion,
            laboratorio=laboratorio,
            condicion=condicion,
            responsable=responsable
        )

    # OPCIÓN 1: REGISTRAR EQUIPO

    def registrar_equipo(self) -> None:
        self.mostrar_encabezado("REGISTRAR EQUIPO")

        codigo = self.leer_codigo(
            "Ingrese el código patrimonial: "
        )

        # Verificar que el código no exista.
        if self.arbol.buscar(codigo) is not None:
            print(
                "\nERROR: Ya existe un equipo "
                "con ese código patrimonial."
            )
            return

        descripcion = self.leer_texto(
            "Descripción: "
        )

        laboratorio = self.leer_texto(
            "Laboratorio: "
        )

        condicion = self.leer_condicion()

        responsable = self.leer_texto(
            "Responsable: "
        )

        try:
            equipo = Equipo(
                codigo,
                descripcion,
                laboratorio,
                condicion,
                responsable
            )

            registrado = self.arbol.insertar(
                equipo,
                traza=self.modo_demostracion
            )

            if registrado:
                print("\nEquipo registrado correctamente.")
                self.mostrar_datos_equipo(equipo)
            else:
                print(
                    "\nERROR: No se pudo registrar. "
                    "El código ya existe."
                )

        except (ValueError, TypeError) as error:
            print(f"\nERROR: {error}")


    # OPCIÓN 2: BUSCAR EQUIPO

    def buscar_equipo(self) -> None:

        self.mostrar_encabezado("BUSCAR EQUIPO")

        codigo = self.leer_codigo(
            "Ingrese el código patrimonial: "
        )

        equipo = self.arbol.buscar(
            codigo,
            traza=self.modo_demostracion
        )

        if equipo is None:
            print(
                "\nNo se encontró ningún equipo "
                "con ese código patrimonial."
            )
            return

        print("\nEquipo encontrado:")
        self.mostrar_datos_equipo(equipo)


    # OPCIÓN 3: MODIFICAR EQUIPO

    def modificar_equipo(self) -> None:

        self.mostrar_encabezado("MODIFICAR EQUIPO")

        codigo = self.leer_codigo(
            "Código del equipo a modificar: "
        )

        equipo = self.arbol.buscar(codigo)

        if equipo is None:
            print("\nERROR: El equipo no existe.")
            return

        print("\nDatos actuales:")
        self.mostrar_datos_equipo(equipo)

        print("\nIngrese los nuevos datos.")
        print("Presione ENTER para conservar un valor.")
        print(
            "El código patrimonial no puede modificarse."
        )

        descripcion = input(
            f"Descripción [{equipo.descripcion}]: "
        ).strip()

        laboratorio = input(
            f"Laboratorio [{equipo.laboratorio}]: "
        ).strip()

        print("\nCondición actual:", equipo.condicion)
        print("0. Mantener condición actual")

        for indice, condicion in enumerate(
            Equipo.CONDICIONES_VALIDAS, 1
        ):
            print(f"{indice}. {condicion}")

        while True:
            opcion = input(
                "Seleccione nueva condición [0]: "
            ).strip()

            if opcion in ["", "0"]:
                condicion_nueva = equipo.condicion
                break

            if opcion.isdigit():
                numero = int(opcion)

                if 1 <= numero <= len(
                    Equipo.CONDICIONES_VALIDAS
                ):
                    condicion_nueva = (
                        Equipo.CONDICIONES_VALIDAS[numero - 1]
                    )
                    break

            print("ERROR: Condición inválida.")

        responsable = input(
            f"Responsable [{equipo.responsable}]: "
        ).strip()

        # Preparar los valores finales.
        nueva_descripcion = descripcion or equipo.descripcion
        nuevo_laboratorio = laboratorio or equipo.laboratorio
        nuevo_responsable = responsable or equipo.responsable

        try:
            # Validar todos los datos antes de modificar
            # el objeto original.
            Equipo(
                equipo.codigo_patrimonial,
                nueva_descripcion,
                nuevo_laboratorio,
                condicion_nueva,
                nuevo_responsable
            )

            # Aplicar las modificaciones.
            equipo.descripcion = nueva_descripcion
            equipo.laboratorio = nuevo_laboratorio
            equipo.condicion = condicion_nueva
            equipo.responsable = nuevo_responsable

            print("\nEquipo actualizado correctamente.")
            self.mostrar_datos_equipo(equipo)

        except (ValueError, TypeError) as error:
            print(f"\nERROR: {error}")


    # OPCIÓN 4: ELIMINAR EQUIPO

    def eliminar_equipo(self) -> None:

        self.mostrar_encabezado("ELIMINAR EQUIPO")

        codigo = self.leer_codigo(
            "Código del equipo a eliminar: "
        )

        equipo = self.arbol.buscar(codigo)

        if equipo is None:
            print("\nERROR: No existe ese equipo.")
            return

        print("\nEquipo seleccionado:")
        self.mostrar_datos_equipo(equipo)

        confirmacion = input(
            "\n¿Está seguro de eliminarlo? (S/N): "
        ).strip().lower()

        if confirmacion not in ("s", "si", "sí"):
            print("\nEliminación cancelada.")
            return

        try:
            eliminado = self.arbol.eliminar(codigo)

            if eliminado:
                print("\nEquipo eliminado correctamente.")
            else:
                print("\nNo se pudo eliminar el equipo.")

        except (ValueError, TypeError) as error:
            print(f"\nERROR: {error}")


    # OPCIONES 5, 6 Y 7: RECORRIDOS DEL BST

    def mostrar_recorrido(self, tipo: str) -> None:
        """
        Muestra los equipos de acuerdo con
        el recorrido seleccionado.
        """
        recorridos = {
            "preorder": (
                "PREORDER",
                self.arbol.preorder
            ),
            "inorder": (
                "INORDER",
                self.arbol.inorder
            ),
            "postorder": (
                "POSTORDER",
                self.arbol.postorder
            )
        }

        if tipo not in recorridos:
            print("\nERROR: Recorrido no válido.")
            return

        titulo, funcion = recorridos[tipo]

        self.mostrar_encabezado(
            f"RECORRIDO {titulo}"
        )

        equipos = funcion()

        if not equipos:
            print("\nEl árbol está vacío.")
            return

        print("\nSecuencia de códigos patrimoniales:")
        print(
            " -> ".join(
                str(equipo.codigo_patrimonial)
                for equipo in equipos
            )
        )

        print("\nEquipos encontrados:")

        for indice, equipo in enumerate(equipos, 1):
            print(
                f"{indice}. "
                f"{equipo.codigo_patrimonial} - "
                f"{equipo.descripcion} | "
                f"{equipo.laboratorio} | "
                f"{equipo.condicion}"
            )


    # OPCIÓN 8: ESTADÍSTICAS DEL BST


    def mostrar_estadisticas(self) -> None:

        self.mostrar_encabezado(
            "ESTADÍSTICAS DEL ÁRBOL BST"
        )

        cantidad = self.arbol.contar_nodos()
        hojas = self.arbol.contar_hojas()
        altura = self.arbol.altura()

        if self.arbol.esta_vacio():
            raiz = "No existe"
        else:
            raiz = (
                self.arbol.raiz.equipo.codigo_patrimonial
            )

        print(f"\nRaíz del árbol       : {raiz}")
        print(f"Cantidad de nodos    : {cantidad}")
        print(f"Cantidad de hojas    : {hojas}")
        print(f"Altura del árbol     : {altura}")
        print(
            f"BST válido           : "
            f"{self.arbol.validar_bst()}"
        )

        print("\nNota: La altura se mide en aristas.")
        print("Un árbol vacío tiene altura -1.")


    # OPCIÓN 9: VISUALIZAR BST


    def visualizar_arbol(self) -> None:

        self.mostrar_encabezado(
            "VISUALIZACIÓN DEL ÁRBOL BST"
        )

        print()
        print(self.arbol.visualizar())

        print("\nLeyenda:")
        print("[raiz] = Nodo principal")
        print("[izq]  = Hijo izquierdo")
        print("[der]  = Hijo derecho")


    # MODO DEMOSTRACIÓN


    def configurar_demostracion(self) -> None:

        self.modo_demostracion = (
            not self.modo_demostracion
        )

        estado = (
            "ACTIVADO"
            if self.modo_demostracion
            else "DESACTIVADO"
        )

        print(
            f"\nModo demostración: {estado}"
        )


    # MENÚ PRINCIPAL

    def mostrar_menu(self) -> None:

        print("\n" + "=" * 60)
        print("UNIVERSIDAD NACIONAL DE TRUJILLO".center(60))
        print("CONTROL DE ACTIVOS DE LABORATORIO".center(60))
        print("GRUPO 07 - ÁRBOL BINARIO DE BÚSQUEDA".center(60))
        print("=" * 60)

        print("\n1. Registrar equipo")
        print("2. Buscar equipo")
        print("3. Modificar equipo")
        print("4. Eliminar equipo")
        print("5. Recorrido Preorder")
        print("6. Recorrido Inorder")
        print("7. Recorrido Postorder")
        print("8. Estadísticas del árbol")
        print("9. Visualizar árbol")
        print("D. Activar/desactivar modo demostración")
        print("0. Salir")

        estado = (
            "ACTIVADO"
            if self.modo_demostracion
            else "DESACTIVADO"
        )

        print(f"\nModo demostración: {estado}")
        print("-" * 60)

    def ejecutar(self) -> None:

        while True:
            try:
                self.mostrar_menu()

                opcion = input(
                    "Seleccione una opción: "
                ).strip().lower()

                if opcion == "1":
                    self.registrar_equipo()

                elif opcion == "2":
                    self.buscar_equipo()

                elif opcion == "3":
                    self.modificar_equipo()

                elif opcion == "4":
                    self.eliminar_equipo()

                elif opcion == "5":
                    self.mostrar_recorrido("preorder")

                elif opcion == "6":
                    self.mostrar_recorrido("inorder")

                elif opcion == "7":
                    self.mostrar_recorrido("postorder")

                elif opcion == "8":
                    self.mostrar_estadisticas()

                elif opcion == "9":
                    self.visualizar_arbol()

                elif opcion == "d":
                    self.configurar_demostracion()

                elif opcion == "0":
                    print("\n" + "=" * 60)
                    print("Gracias por utilizar el sistema.")
                    print("Programa finalizado correctamente.")
                    print("=" * 60)
                    break

                else:
                    print(
                        "\nERROR: Seleccione una "
                        "opción válida del menú."
                    )

                self.pausar()

            except (KeyboardInterrupt, EOFError):
                print(
                    "\n\nPrograma finalizado por el usuario."
                )
                break

            except (ValueError, TypeError) as error:
                print(f"\nERROR: {error}")
                self.pausar()

