import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ajusta la URL a la de tu portal real
PORTAL_URL = "https://cnnespanol.cnn.com/"

# Configuración del servicio de ChromeDriver (Favor de cambiarlo según su sistema operativo)
s = Service('chromedriver-mac-arm64 2/chromedriver')

'''

Nota:
- Debido a que la página lanza resultados predeterminados cuando hay una búsqueda en donde 
no se puede encontrar con las palabras clave enviadas, el mensaje de "No se encontraron resultados de búsqueda" 
no se puede verificar de manera tangible, se encuentra en los metadatos de la página, pero no es visible. Gracias por su comprensión.

'''


'''Este script de prueba utiliza Selenium para automatizar la verificación de la página principal de un portal de noticias.'''

class TestPaginaPrincipal(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=s)
        self.driver.get(PORTAL_URL)

    def test_titulo_pagina(self):
        titulo_esperado = "Últimas noticias de Estados Unidos, Latinoamérica y el mundo, hoy | CNN en Español | CNN"
        titulo_obtenido = self.driver.title

        self.assertEqual(titulo_obtenido, titulo_esperado,
                         "(-) El título de la página principal no coincide.")

        print("(+) Título de la página verificado correctamente.")

    def test_elementos_principales(self):
        # Header
        header = self.driver.find_element(By.CLASS_NAME, "container__title_url-text")
        self.assertTrue(header.is_displayed(), "(-) El encabezado no se está mostrando.")
        print("(+) Encabezado encontrado y visible.")

        # Footer
        footer = self.driver.find_element(By.TAG_NAME, "footer")
        self.assertTrue(footer.is_displayed(), "(-) El pie de página no se está mostrando.")
        print("(+) Pie de página encontrado y visible.")

        # Search Bar
        icono_busqueda = self.driver.find_element(By.CLASS_NAME, "header__search-icon")
        icono_busqueda.click()
        barra_busqueda = self.driver.find_element(By.CLASS_NAME, "search-bar")
        self.assertTrue(barra_busqueda.is_displayed(), "(-) La barra de búsqueda no se está mostrando.")
        print("(+) Barra de búsqueda encontrada y visible tras hacer clic en el ícono.")

    def test_lista_noticias_principales(self):
        noticias = self.driver.find_elements(By.CLASS_NAME, "container__headline-text")
        self.assertGreater(len(noticias), 0, "(-) No se encontraron noticias principales en la página.")
        print(f"(+) Se encontraron {len(noticias)} noticias principales.")

        for index, noticia in enumerate(noticias, start=1):
            self.assertTrue(noticia.text, f"(-) La noticia #{index} no tiene título visible.")
        print("(+) Todas las noticias principales tienen título.")

    def tearDown(self):
        self.driver.quit()
        

'''Este script de prueba utiliza Selenium para automatizar la verificación de la funcionalidad de búsqueda en un portal de noticias.'''

class TestBusquedaNoticias(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=s)
        self.driver.get(PORTAL_URL)

    def test_busqueda_valida(self):

        icono_busqueda = self.driver.find_element(By.CLASS_NAME, "header__search-icon")
        icono_busqueda.click()
        print("(+) Icono de búsqueda encontrado y clicado.")

        barra_busqueda = self.driver.find_element(By.CLASS_NAME, "search-bar__input")
        barra_busqueda.send_keys("cambio climático" + Keys.RETURN)
        print("(+) Barra de búsqueda encontrada y se ingresó el texto 'cambio climático'.")
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(By.CSS_SELECTOR, "div.card.container__item.container__item--type-media-image")
        )

        resultados = self.driver.find_elements(
            By.CSS_SELECTOR,
            "div.card.container__item.container__item--type-media-image"
        )
        self.assertGreater(
            len(resultados),
            0,
            "(-) No se encontraron resultados de búsqueda para 'cambio climático'."
        )
        print(f"(+) Se encontraron {len(resultados)} resultados de búsqueda para 'cambio climático'.")


        for index, resultado in enumerate(resultados, start=1):
            titulo = resultado.find_element(By.CSS_SELECTOR, ".container__headline-text")
            self.assertTrue(
                 titulo.text.strip(),
                 f"(-) El resultado #{index} no tiene un título visible."
            )
            print(f"(+) Resultado #{index} con título: '{titulo.text}'")

        print("(+) Búsqueda con resultados verificada correctamente.")

    def tearDown(self):
        self.driver.quit()
        
        
'''Este script de prueba utiliza Selenium para automatizar la verificación de la página de detalle de un artículo en un portal de noticias.'''
class TestPaginaArticulo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(PORTAL_URL)
        print("(+) Navegador inicializado y sitio cargado para TestPaginaArticulo.")

    def test_acceso_pagina_articulo(self):
        primer_articulo = self.driver.find_element(By.CSS_SELECTOR, "span.container__headline-text")
        primer_articulo.click()
        print("(+) Hicimos clic en la noticia principal.")

        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(By.CSS_SELECTOR, "div.live-story__items-container")
        )
        print("(+) Página del artículo detectada en el DOM.")

        contenido = self.driver.find_element(By.CSS_SELECTOR, "div.live-story__items-container")
        fecha = self.driver.find_element(By.CSS_SELECTOR, "div.timestamp.vossi-timestamp")

        self.assertTrue(contenido.is_displayed(), "(-) El contenido del artículo no se está mostrando.")
        print("(+) El contenido del artículo se está mostrando.")

        self.assertTrue(fecha.is_displayed(), "(-) La fecha de publicación no se está mostrando.")
        print("(+) La fecha de publicación se está mostrando.")

        print("(+) Acceso a la página del artículo verificado correctamente.")

    def tearDown(self):
        self.driver.quit()
        print("(+) Navegador cerrado para TestPaginaArticulo.")
        


'''Este script de prueba utiliza Selenium para automatizar la verificación de las secciones principales del portal de noticias.'''
class TestSeccionesPrincipales(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(PORTAL_URL)
        print("(+) Navegador inicializado y sitio cargado para TestSeccionesPrincipales.")

    # Test de sección Tech
    def test_acceso_seccion_tecnologia(self):
        print("(+) Iniciando test de acceso a sección 'Tech' (Tecnología).")
        driver = self.driver

        menu_button = driver.find_element(By.CSS_SELECTOR, "a.header__nav-item-link.header__nav-more-link.header__nav-button")
        menu_button.click()
        print("(+) Menú desplegable activado.")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Tech"))
        )
        print("(+) El enlace 'Tech' se ha vuelto visible.")

        enlace_tecnologia = driver.find_element(By.LINK_TEXT, "Tech")
        enlace_tecnologia.click()
        print("(+) Se hizo clic en 'Tech'.")


        articulos_tecnologia = driver.find_elements(By.CSS_SELECTOR, "div.zone__items.layout--wide-left-balanced-2")
        self.assertGreater(
            len(articulos_tecnologia),
            0,
            "(-) No se encontraron artículos en la sección 'Tech'."
        )
        print(f"(+) Se encontraron {len(articulos_tecnologia)} artículos en la sección 'Tech'.")

    # Test de sección Salud
    def test_acceso_seccion_salud(self):
        print("(+) Iniciando test de acceso a sección 'Salud'.")
        driver = self.driver

        menu_button = driver.find_element(By.CSS_SELECTOR, "a.header__nav-item-link.header__nav-more-link.header__nav-button")
        menu_button.click()
        print("(+) Menú desplegable activado.")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Salud"))
        )
        print("(+) El enlace 'Salud' se ha vuelto visible.")

        enlace_salud = driver.find_element(By.LINK_TEXT, "Salud")
        enlace_salud.click()
        print("(+) Se hizo clic en 'Salud'.")

        articulos_salud = driver.find_elements(By.CSS_SELECTOR, "div.zone__items.layout--wide-left-balanced-2")
        self.assertGreater(
            len(articulos_salud),
            0,
            "(-) No se encontraron artículos en la sección 'Salud'."
        )
        print(f"(+) Se encontraron {len(articulos_salud)} artículos en la sección 'Salud'.")

    # Test de sección Deportes
    def test_acceso_seccion_deportes(self):
        print("(+) Iniciando test de acceso a sección 'Deportes'.")
        driver = self.driver

        menu_button = driver.find_element(By.CSS_SELECTOR, "a.header__nav-item-link.header__nav-more-link.header__nav-button")
        menu_button.click()
        print("(+) Menú desplegable activado.")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Deportes"))
        )
        print("(+) El enlace 'Deportes' se ha vuelto visible.")

        enlace_deportes = driver.find_element(By.LINK_TEXT, "Deportes")
        enlace_deportes.click()
        print("(+) Se hizo clic en 'Deportes'.")

        articulos_deportes = driver.find_elements(By.CSS_SELECTOR, "div.zone__items.layout--wide-left-balanced-2")
        self.assertGreater(
            len(articulos_deportes),
            0,
            "(-) No se encontraron artículos en la sección 'Deportes'."
        )
        print(f"(+) Se encontraron {len(articulos_deportes)} artículos en la sección 'Deportes'.")

    def tearDown(self):
        self.driver.quit()
        print("(+) Navegador cerrado para TestSeccionesPrincipales.")


if __name__ == "__main__":
    unittest.main()