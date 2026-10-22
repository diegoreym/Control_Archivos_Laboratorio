from arbol_bst import ArbolBST
from equipo import Equipo

def crear_equipo(codigo):
    return Equipo(codigo, "Test", "Lab", "Operativo", "Admin")

def ejecutar_experimento():
    print("=== EXPERIMENTO DE EFICIENCIA: COMPORTAMIENTO ESTRUCTURAL ===")
    
    arbol_a = ArbolBST()
    claves_a = [420, 220, 620, 120, 320, 520, 720]
    for clave in claves_a:
        arbol_a.insertar(crear_equipo(clave))

    arbol_b = ArbolBST()
    claves_b = sorted(claves_a)
    for clave in claves_b:
        arbol_b.insertar(crear_equipo(clave))

    print("\n--- ARBOL A: ORDEN ORIGINAL ---")
    print(arbol_a.visualizar())
    print(f"Altura: {arbol_a.altura()}")
    print("\n--- ARBOL B: ORDEN ASCENDENTE ---")
    print(arbol_b.visualizar())
    print(f"Altura: {arbol_b.altura()}")

    print("\n--- NODOS EXAMINADOS EN LAS BUSQUEDAS ---\n")
    print(f"{'Busqueda':<16} {'Codigo':<10} {'Arbol A':<10} {'Arbol B':<10}")
    print("-" * 49)

    busquedas = [
        ("Clave minima", min(claves_a)),
        ("Clave maxima", max(claves_a)),
        ("Raiz original", claves_a[0])
    ]

    for nombre, clave in busquedas:
        arbol_a.buscar(clave)
        examinados_a = arbol_a.nodos_examinados

        arbol_b.buscar(clave)
        examinados_b = arbol_b.nodos_examinados

        print(
            f"{nombre:<16} {clave:<10} "
            f"{examinados_a:<10} {examinados_b:<10}"
        )

if __name__ == "__main__":
    ejecutar_experimento()
