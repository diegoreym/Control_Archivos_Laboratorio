from arbol_bst import ArbolBST
from equipo import Equipo

def crear_equipo(codigo):

    return Equipo(codigo, "Test", "Lab", "Operativo", "Admin")

def ejecutar_experimento():
    print("=== EXPERIMENTO DE EFICIENCIA: COMPORTAMIENTO ESTRUCTURAL ===\n")


    arbol_a = ArbolBST()
    claves_a = [420, 220, 620, 120, 320, 520, 720]
    for clave in claves_a:
        arbol_a.insertar(crear_equipo(clave))

    arbol_b = ArbolBST()
    claves_b = sorted(claves_a)
    for clave in claves_b:
        arbol_b.insertar(crear_equipo(clave))

    # 3. COMPARACIÓN DE ALTURAS
    print("--- 1. COMPARACIÓN DE ALTURAS ---")
    print(f"Altura del Árbol A (Balanceado): {arbol_a.altura()}")
    print(f"Altura del Árbol B (Degenerado): {arbol_b.altura()}\n")

if __name__ == "__main__":
    ejecutar_experimento()
