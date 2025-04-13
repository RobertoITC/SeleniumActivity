# SeleniumActivity

# Proyecto de Pruebas Automatizadas con Selenium

Este proyecto contiene un conjunto de pruebas automatizadas en **Python** utilizando **Selenium** para verificar la funcionalidad de un portal de noticias (CNN en Español como ejemplo). Se basa en **unittest** para la ejecución y organización de los diferentes casos de prueba.

## Descripción General

El proyecto incluye las siguientes clases de prueba, cada una enfocada en un aspecto clave del sitio:

1. **TestPaginaPrincipal**  
   - Verifica que la página principal cargue correctamente.  
   - Comprueba la presencia del encabezado, pie de página y la barra de búsqueda.  
   - Valida la lista de noticias principales.

2. **TestBusquedaNoticias**  
   - Abre la barra de búsqueda y envía términos (por ejemplo, “cambio climático”).  
   - Verifica que los resultados de la búsqueda contengan títulos de artículos.

3. **TestPaginaArticulo**  
   - Simula el clic en una noticia principal para abrir la página de detalle.  
   - Comprueba la presencia de contenido y fecha de publicación en la noticia seleccionada.

4. **TestSeccionesPrincipales**  
   - Despliega el menú para acceder a diferentes secciones (Tech, Salud, Deportes, etc.).  
   - Valida que existan artículos en cada una de las secciones tras hacer clic en el enlace correspondiente.

## Requisitos

- **Python 3.x** instalado.  
- **Selenium** (`pip install selenium`).  
- **ChromeDriver** instalado y en el PATH (o configurado en la variable `Service` dentro del script).  
- Un navegador **Google Chrome** compatible con la versión de ChromeDriver.

## Estructura de Archivos

El archivo principal de prueba es:

test_noticias.py

Contiene cuatro clases de prueba:

- `TestPaginaPrincipal`
- `TestBusquedaNoticias`
- `TestPaginaArticulo`
- `TestSeccionesPrincipales`

Cada clase agrupa métodos de test que validan distintas funcionalidades del portal.

## Cómo Ejecutar las Pruebas

1. Clona o descarga el repositorio en tu entorno local.
2. Asegúrate de tener instalado todo lo necesario:
   ```bash
   pip install selenium
   ```
   

3.	Verifica la ruta de tu ChromeDriver en test_noticias.py. En el ejemplo, se utiliza:

    s = Service('chromedriver-mac-arm64 2/chromedriver')

    Ajusta la ruta y el archivo según tu sistema operativo.

4.	Ejecuta los tests desde la línea de comandos (en la carpeta donde se encuentra el archivo test_noticias.py):

    ```bash

    python test_noticias.py
    ```




