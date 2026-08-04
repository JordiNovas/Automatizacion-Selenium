# 🧪 Proyecto de Automatización de Pruebas con Selenium & PyTest

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-green?style=for-the-badge&logo=selenium)
![PyTest](https://img.shields.io/badge/PyTest-Framework-orange?style=for-the-badge&logo=pytest)
![Flask](https://img.shields.io/badge/Flask-App%20Base-black?style=for-the-badge&logo=flask)

Este proyecto consiste en una suite de **pruebas automatizadas E2E (End-to-End)** aplicadas sobre una aplicación web funcional de gestión de inventario desarrollada en **Flask**. La automatización está implementada en **Python con Selenium WebDriver**, siguiendo el patrón de diseño **Page Object Model (POM)**.

---

## 📌 Características del Proyecto

- 🏗️ **Patrón Page Object Model (POM):** Separación clara entre los elementos de la interfaz web y la lógica de las pruebas.
- 🇪🇸 **100% en Español:** Tanto el sistema base como las validaciones, reportes y aserciones están configuradas totalmente en español.
- 🎯 **Cobertura Completa de Pruebas:**
  - 🟢 **Camino Feliz (Happy Path):** Escenarios exitosos de negocio.
  - 🔴 **Pruebas Negativas:** Manejo de errores y validación de credenciales/datos incorrectos.
  - 🟡 **Pruebas de Límites:** Validación de restricciones en formularios (longitud de caracteres, campos obligatorios, valores numéricos no válidos).
- 📸 **Evidencias Automáticas:** Captura automática de pantalla (`.png`) por cada escenario ejecutado.
- 📊 **Reporte HTML Interactivo:** Generación automática de un reporte consolidado de ejecución (`pytest-html`).

---

## 🛠️ Tecnologías y Librerías Utilizadas

- **Lenguaje:** Python
- **Automatización:** Selenium WebDriver + `webdriver-manager`
- **Framework de Pruebas:** PyTest
- **Reportes:** `pytest-html`
- **Aplicación Base:** Flask (Python)

---

## 📁 Estructura del Proyecto

```text
Automatizacion-Selenium/
│
├── pages/                    # Patrón POM: Locators y acciones de las páginas
│   ├── __init__.py
│   ├── base_page.py          # Wrapper genérico con esperas explícitas
│   ├── login_page.py         # Mapeo y métodos del Login
│   └── inventory_page.py     # Mapeo y métodos del CRUD de Inventario
│
├── tests/                    # Suites de pruebas automatizadas
│   ├── __init__.py
│   ├── test_hu01_login.py    # Historias de Usuario para Autenticación
│   └── test_hu02_crud.py     # Historias de Usuario para Operaciones CRUD
│
├── reports/                  # Reporte HTML generado tras la ejecución
├── screenshots/              # Evidencias fotográficas tomadas automáticamente
│
├── app.py                    # Aplicación Web base en Flask
├── conftest.py               # Fixtures de PyTest y hooks de capturas
├── pytest.ini                # Configuración global del ejecutor de pruebas
├── .gitignore                # Exclusión de archivos temporales/entorno
└── README.md                 # Documentación del proyecto
