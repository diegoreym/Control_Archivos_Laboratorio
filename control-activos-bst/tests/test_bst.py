import unittest
from arbol_bst import ArbolBST
from equipo import Equipo

class TestBSTControlActivos(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de CADA prueba para darnos un árbol limpio."""
        self.arbol = ArbolBST()
        self.equipos_base = [
            Equipo(420, "Microscopio", "Lab 1", "Operativo", "Admin"),
            Equipo(220, "Osciloscopio", "Lab 1", "Operativo", "Admin"),
            Equipo(620, "Proyector", "Lab 2", "Operativo", "Admin"),
            Equipo(120, "Router", "Lab 3", "Operativo", "Admin"),
            Equipo(320, "Multimetro", "Lab 1", "Operativo", "Admin"),
            Equipo(520, "Servidor", "Lab 3", "Operativo", "Admin"),
            Equipo(720, "Impresora 3D", "Lab 2", "Operativo", "Admin")
        ]

    def poblar_arbol(self):
        for eq in self.equipos_base:
            self.arbol.insertar(eq)

    # P01: Insertar los siete registros
    def test_p01_insertar_siete_registros(self):
        self.poblar_arbol()
        self.assertEqual(self.arbol.contar_nodos(), 7, "El tamaño debe ser 7")
        self.assertTrue(self.arbol.validar_bst(), "El árbol debe ser un BST válido")

    # P02: Insertar nuevamente 420 (Duplicado)
    def test_p02_rechazar_duplicado(self):
        self.poblar_arbol()
        resultado = self.arbol.insertar(Equipo(420, "Copia", "Lab", "Operativo", "Admin"))
        self.assertFalse(resultado, "Debe rechazar la inserción del duplicado 420")
        self.assertEqual(self.arbol.contar_nodos(), 7, "El tamaño no debe cambiar")

    # P03: Buscar 320
    def test_p03_buscar_existente(self):
        self.poblar_arbol()
        encontrado = self.arbol.buscar(320)
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.codigo_patrimonial, 320)

    # P04: Buscar clave inexistente
    def test_p04_buscar_inexistente(self):
        self.poblar_arbol()
        encontrado = self.arbol.buscar(999)
        self.assertIsNone(encontrado, "Debe retornar None o manejar el caso sin caerse")

    # P05: Eliminar hoja 120
    def test_p05_eliminar_hoja(self):
        self.poblar_arbol()
        self.assertTrue(self.arbol.eliminar(120))
        self.assertEqual(self.arbol.contar_nodos(), 6)
        self.assertIsNone(self.arbol.buscar(120))

    # P06: Eliminar nodo con un hijo
    def test_p06_eliminar_un_hijo(self):
        self.poblar_arbol()
        self.arbol.eliminar(120)  
        self.assertTrue(self.arbol.eliminar(220))
        codigos = [eq.codigo_patrimonial for eq in self.arbol.inorder()]
        self.assertEqual(codigos, sorted(codigos), "El inorder debe seguir ascendente")

    # P07: Eliminar raíz con dos hijos
    def test_p07_eliminar_raiz(self):
        self.poblar_arbol()
        self.assertTrue(self.arbol.eliminar(420))
        self.assertEqual(self.arbol.contar_nodos(), 6)
        self.assertTrue(self.arbol.validar_bst(), "El árbol debe seguir siendo válido tras reemplazar con sucesor")

    # P08: Ejecutar tres recorridos
    def test_p08_recorridos(self):
        self.poblar_arbol()
        preorder = [eq.codigo_patrimonial for eq in self.arbol.preorder()]
        inorder = [eq.codigo_patrimonial for eq in self.arbol.inorder()]
        postorder = [eq.codigo_patrimonial for eq in self.arbol.postorder()]
        
        self.assertEqual(preorder, [420, 220, 120, 320, 620, 520, 720])
        self.assertEqual(inorder, [120, 220, 320, 420, 520, 620, 720])
        self.assertEqual(postorder, [120, 320, 220, 520, 720, 620, 420])

    # P09: Intentar ingresar clave no numérica
    def test_p09_clave_no_numerica(self):
        with self.assertRaises(ValueError):
             Equipo("codigo_falso", "Test", "Lab", "Operativo", "Admin")

    # P10: Operar sobre árbol vacío
    def test_p10_arbol_vacio(self):
        self.assertIsNone(self.arbol.buscar(100))
        self.assertFalse(self.arbol.eliminar(100))
        self.assertEqual(self.arbol.contar_nodos(), 0)

    # P11: Validaciones de dominio (Condición inválida)
    def test_p11_validaciones_dominio(self):
        with self.assertRaises(ValueError):
            Equipo(900, "Test", "Lab", "CondicionFalsa", "Admin")

if __name__ == '__main__':
    unittest.main()
