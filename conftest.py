import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver(request):
    # Configuración del navegador Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(5)
    
    yield driver
    
    # Captura de pantalla automática al finalizar cada test
    screenshot_dir = os.path.join(os.path.dirname(__file__), "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)
    
    test_name = request.node.name
    screenshot_path = os.path.join(screenshot_dir, f"{test_name}.png")
    driver.save_screenshot(screenshot_path)
    
    driver.quit()