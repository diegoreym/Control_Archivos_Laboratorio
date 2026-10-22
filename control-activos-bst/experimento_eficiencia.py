"""Compara las búsquedas en un BST con dos órdenes de inserción."""

from arbol_bst import ArbolBST
from equipo import Equipo


def crear_equipo(codigo: int) -> Equipo:
    return Equipo(codigo, "Equipo de prueba", "Laboratorio", "Operativo", "Admin")


def nodos_examinados_al_buscar(arbol: ArbolBST, codigo: int) -> int:
    """Busca una clave y devuelve cuántos nodos examinó el BST."""
    equipo = arbol.buscar(codigo)
    if equipo is None:
        raise RuntimeError(f"No se encontró la clave de prueba {codigo}.")
    return arbol.nodos_examinados


def ejecutar_experimento() -> None:
    claves = [420, 220, 620, 120, 320, 520, 720]

    # Árbol A: inserción en el orden de los registros de la guía.
    arbol_a = ArbolBST()
    for clave in claves:
        arbol_a.insertar(crear_equipo(clave))

    # Árbol B: las mismas claves insertadas en orden ascendente.
    arbol_b = ArbolBST()
    for clave in sorted(claves):
        arbol_b.insertar(crear_equipo(clave))

    print("=== EXPERIMENTO DE EFICIENCIA DEL BST ===\n")
    print(f"Altura del árbol A (orden de la guía): {arbol_a.altura()}")
    print(f"Altura del árbol B (orden ascendente): {arbol_b.altura()}\n")

    casos = (
        ("Clave mínima", min(claves)),
        ("Clave máxima", max(claves)),
        ("Raíz original", claves[0]),
    )

    print("Nodos examinados por búsqueda:")
    print(f"{'Caso':<18} {'Clave':>7} {'Árbol A':>10} {'Árbol B':>10}")
    print("-" * 49)

    for nombre, codigo in casos:
        examinados_a = nodos_examinados_al_buscar(arbol_a, codigo)
        examinados_b = nodos_examinados_al_buscar(arbol_b, codigo)
        print(
            f"{nombre:<18} {codigo:>7} "
            f"{examinados_a:>10} {examinados_b:>10}"
        )

    print("\nEl costo de búsqueda es O(h), donde h es la altura del árbol.")


if __name__ == "__main__":
    ejecutar_experimento()
