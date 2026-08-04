import sys, os
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_camino_feliz(driver):
    """ HU01 - Camino Feliz: Credenciales correctas en español """
    login_pg = LoginPage(driver)
    inventory_pg = InventoryPage(driver)
    
    login_pg.load()
    login_pg.login("admin", "admin123")
    
    assert inventory_pg.obtener_titulo() == "Gestión de Productos"

def test_login_prueba_negativa(driver):
    """ HU01 - Prueba Negativa: Credenciales erróneas """
    login_pg = LoginPage(driver)
    
    login_pg.load()
    login_pg.login("admin", "clave_incorrecta")
    
    assert login_pg.obtener_mensaje_error() == "Credenciales inválidas"

def test_login_prueba_limites(driver):
    """ HU01 - Prueba de Límites: Formulario vacío """
    login_pg = LoginPage(driver)
    
    login_pg.load()
    login_pg.login("", "")
    
    assert login_pg.obtener_mensaje_error() == "Campos obligatorios requeridos"