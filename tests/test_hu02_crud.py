import sys, os
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture(autouse=True)
def iniciar_sesion(driver):
    login_pg = LoginPage(driver)
    login_pg.load()
    login_pg.login("admin", "admin123")

def test_crud_crear_camino_feliz(driver):
    """ HU02 - Crear Producto: Camino Feliz """
    inventory = InventoryPage(driver)
    conteo_inicial = inventory.obtener_conteo_productos()
    
    inventory.crear_producto("Monitor LG 27", "Monitores", 250.00)
    
    assert inventory.obtener_conteo_productos() == conteo_inicial + 1

def test_crud_crear_prueba_negativa(driver):
    """ HU02 - Crear Producto: Precio negativo """
    inventory = InventoryPage(driver)
    
    inventory.crear_producto("Mouse Gamer", "Periféricos", -10.00)
    
    assert inventory.obtener_alerta_error() == "El precio debe ser un valor positivo"

def test_crud_eliminar_camino_feliz(driver):
    """ HU05 - Eliminar Producto: Camino Feliz """
    inventory = InventoryPage(driver)
    conteo_inicial = inventory.obtener_conteo_productos()
    
    inventory.eliminar_primer_producto()
    
    assert inventory.obtener_conteo_productos() == conteo_inicial - 1