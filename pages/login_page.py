from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USUARIO_INPUT = (By.ID, "usuario")
    CLAVE_INPUT = (By.ID, "clave")
    BTN_INGRESAR = (By.ID, "btn-ingresar")
    MENSAJE_ERROR = (By.ID, "mensaje-error")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://127.0.0.1:5000/"

    def load(self):
        self.open_url(self.url)

    def login(self, usuario, clave):
        self.type(self.USUARIO_INPUT, usuario)
        self.type(self.CLAVE_INPUT, clave)
        self.click(self.BTN_INGRESAR)

    def obtener_mensaje_error(self):
        return self.get_text(self.MENSAJE_ERROR)
    