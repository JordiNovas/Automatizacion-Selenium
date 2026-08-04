from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    TITULO_PAGINA = (By.ID, "titulo-pagina")
    INPUT_NOMBRE = (By.ID, "nombre")
    INPUT_CATEGORIA = (By.ID, "categoria")
    INPUT_PRECIO = (By.ID, "precio")
    BTN_GUARDAR = (By.ID, "btn-guardar")
    ALERTA_ERROR = (By.ID, "alerta-error")
    FILAS_TABLA = (By.XPATH, "//tbody[@id='tabla-productos']/tr")

    def obtener_titulo(self):
        return self.get_text(self.TITULO_PAGINA)

    def crear_producto(self, nombre, categoria, precio):
        self.type(self.INPUT_NOMBRE, nombre)
        self.type(self.INPUT_CATEGORIA, categoria)
        self.type(self.INPUT_PRECIO, str(precio))
        self.click(self.BTN_GUARDAR)

    def obtener_conteo_productos(self):
        try:
            elementos = self.driver.find_elements(*self.FILAS_TABLA)
            return len(elementos)
        except:
            return 0

    def eliminar_primer_producto(self):
        btn_eliminar = (By.XPATH, "//tbody[@id='tabla-productos']/tr[1]//a[contains(@class,'btn-eliminar')]")
        self.click(btn_eliminar)

    def obtener_alerta_error(self):
        return self.get_text(self.ALERTA_ERROR)