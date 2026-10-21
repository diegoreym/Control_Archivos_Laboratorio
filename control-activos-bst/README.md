# Control de activos de laboratorio con BST

Aplicación de consola en Python 3 para administrar activos de un laboratorio universitario. El proyecto implementa un árbol binario de búsqueda (BST) propio, ordenado por código patrimonial, como práctica de estructuras de datos y programación orientada a objetos.

## Modelo de datos

`equipo.py` define la clase `Equipo` con estos atributos:

- `codigo_patrimonial`: entero positivo, clave de ordenación de solo lectura.
- `descripcion`: descripción del activo.
- `laboratorio`: laboratorio al que pertenece.
- `condicion`: `Operativo`, `En mantenimiento` o `Inoperativo`.
- `responsable`: persona responsable del activo.

Los campos de texto son obligatorios y se recortan al crear o modificar el objeto. La clave no se puede modificar: para cambiarla se elimina el equipo del árbol y se registra de nuevo. La clase `Equipo` solo modela y valida los datos; la inserción y el rechazo de códigos duplicados corresponden al BST.

Ejemplo:

```python
from equipo import Equipo

equipo = Equipo(
    codigo_patrimonial=420,
    descripcion="Microscopio",
    laboratorio="Biología",
    condicion="Operativo",
    responsable="Ana Pérez",
)
print(equipo)
```

## Estructura del proyecto

- `equipo.py`: entidad y validación de sus campos.
- `nodo.py`, `bst_core.py`: nodo, inserción y búsqueda.
- `bst_eliminacion.py`: eliminación en los tres casos del BST.
- `bst_recorridos.py`, `bst_estadisticas.py`: recorridos, métricas y visualización.
- `arbol_bst.py`: clase pública que integra los módulos del árbol.
- `sistema_equipo.py`, `main.py`: interacción por consola.
- `tests/test_bst.py`: pruebas del árbol.
- `experimento_eficiencia.py`: comparación de árboles con distintas alturas.

## Requisitos y ejecución

Se requiere Python 3. Desde esta carpeta, cuando la interfaz esté integrada, se ejecutará con:

```bash
python main.py
```

Los módulos de la interfaz y del árbol se encuentran en construcción. La base compartida usa `Equipo` y los nombres de archivos acordados en la guía del grupo. El BST no debe sustituirse por un diccionario, una lista ordenada ni una biblioteca externa de árboles.

## Reglas del BST

- Los códigos menores van al subárbol izquierdo y los mayores al derecho.
- Los códigos duplicados se rechazan.
- `inorder` debe producir códigos estrictamente ascendentes.
- La raíz tiene profundidad 0; la altura se mide en aristas, por lo que un árbol vacío tiene altura -1 y una hoja altura 0.
- Las operaciones de búsqueda, inserción y eliminación tienen costo `O(h)`, donde `h` es la altura del árbol.

## Colaboración

El trabajo se integra mediante ramas de funcionalidad y Pull Requests hacia `dev`. No se deben subir cambios directamente a `main`. La rama `main` se reserva para la versión final validada por el grupo.
