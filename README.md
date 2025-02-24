# Actividad-final-primer-parcial

# Enlace al documento: https://unibedom-my.sharepoint.com/:w:/g/personal/jcruz14_est_unibe_edu_do/EXCenwz4ed9Cgw4Qb5VwvLMBZz3PZAM98-GZlllTn3BLqQ?e=TABAFX

# Pruebas Unitarias para API FakeStore

## Descripción
Este proyecto implementa pruebas unitarias utilizando `pytest` para validar la funcionalidad de la API `FakeStoreAPI`. Las pruebas cubren operaciones CRUD sobre productos y validan respuestas esperadas.

## Tecnologías Utilizadas
- Python
- Pytest
- Requests
- Git

## Instalación
Antes de ejecutar las pruebas, asegúrate de tener Python y `pytest` instalados. Si no los tienes, instálalos con:

```sh
pip install pytest requests
```

## Estructura del Proyecto
```
/
├── test_api.py  # Archivo con las pruebas unitarias
├── README.md    # Documentación del proyecto
└── requirements.txt  # Lista de dependencias (opcional)
```

## Casos de Uso Cubiertos
1. **Obtener todos los productos** (`GET /products`)
2. **Obtener un producto específico** (`GET /products/1`)
3. **Crear un producto** (`POST /products`)
4. **Actualizar un producto** (`PUT /products/1`)
5. **Eliminar un producto** (`DELETE /products/1`)
6. **Consultar un usuario inexistente** (`GET /users/9999`)

## Ejecución de las Pruebas
Para ejecutar las pruebas, usa el siguiente comando en la terminal dentro del directorio del proyecto:

```sh
pytest test_api.py
```

Esto ejecutará todas las pruebas y mostrará el resultado en la consola.

## Subida a Git
Asegúrate de haber inicializado un repositorio de Git y subido los cambios con los siguientes comandos:

```sh
git init
git add .
git commit -m "Añadir pruebas unitarias"
git branch -M main
git remote add origin <URL_DEL_REPOSITORIO>
git push -u origin main
```
