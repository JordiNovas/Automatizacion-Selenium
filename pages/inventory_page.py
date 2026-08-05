from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    # --- LOCALIZADORES EXISTENTES ---
    TITULO_PAGINA = (By.ID, "titulo-pagina")
    INPUT_NOMBRE = (By.ID, "nombre")
    INPUT_CATEGORIA = (By.ID, "categoria")
    INPUT_PRECIO = (By.ID, "precio")
    BTN_GUARDAR = (By.ID, "btn-guardar")
    ALERTA_ERROR = (By.ID, "alerta-error")
    FILAS_TABLA = (By.XPATH, "//tbody[@id='tabla-productos']/tr")

    # --- NUEVOS LOCALIZADORES (Búsqueda y Mensaje sin resultados) ---
    INPUT_BUSQUEDA = (By.ID, "buscar-producto")  # Ajusta el ID según el HTML de tu input
    MENSAJE_NO_RESULTADOS = (By.ID, "mensaje-no-resultados")  # Ajusta el ID según corresponda

    # -------------------------------------------------------------
    # MÉTODOS EXISTENTES
    # -------------------------------------------------------------
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
            # Filtramos solo las filas visibles en pantalla (por si hay filtros activos)
            visibles = [f for f in elementos if f.is_displayed()]
            return len(visibles)
        except:
            return 0

    def eliminar_primer_producto(self):
        btn_eliminar = (By.XPATH, "//tbody[@id='tabla-productos']/tr[1]//a[contains(@class,'btn-eliminar')]")
        self.click(btn_eliminar)

    def obtener_alerta_error(self):
        return self.get_text(self.ALERTA_ERROR)

    # -------------------------------------------------------------
    # NUEVOS MÉTODOS: HU06 - BÚSQUEDA Y FILTRADO
    # -------------------------------------------------------------
    def buscar_producto(self, texto):
        """Escribe el término de búsqueda en el campo correspondiente."""
        self.type(self.INPUT_BUSQUEDA, texto)

    def obtener_mensaje_sin_resultados(self):
        """Devuelve el texto mostrado cuando no se encuentran coincidencias."""
        return self.get_text(self.MENSAJE_NO_RESULTADOS)

    # -------------------------------------------------------------
    # NUEVO MÉTODO: ACTUALIZAR PRODUCTO (Update del CRUD)
    # -------------------------------------------------------------
    def editar_primer_producto(self, nuevo_nombre, nueva_categoria, nuevo_precio):
        """
        Hace clic en el botón Editar de la primera fila, modifica el formulario y guarda.
        """
        btn_editar = (By.XPATH, "//tbody[@id='tabla-productos']/tr[1]//a[contains(@class,'btn-editar')]")
        self.click(btn_editar)
        
        # Reescribe los campos con la nueva información
        self.type(self.INPUT_NOMBRE, nuevo_nombre)
        self.type(self.INPUT_CATEGORIA, nueva_categoria)
        self.type(self.INPUT_PRECIO, str(nuevo_precio))
        self.click(self.BTN_GUARDAR)