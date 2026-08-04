from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "clave_secreta_qa"

# Base de datos simulada
USUARIOS = {"admin": "admin123"}
PRODUCTOS = [
    {"id": 1, "nombre": "Laptop Dell", "categoria": "Equipos", "precio": 850.00},
    {"id": 2, "nombre": "Teclado Mecánico", "categoria": "Periféricos", "precio": 45.00}
]

HTML_LOGIN = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Sistema de Gestión - Login</title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background: #f4f4f9; }
        .card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); width: 300px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input { width: 100%; padding: 8px; box-sizing: border-box; }
        button { width: 100%; padding: 10px; background: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; }
        .alert { color: red; margin-bottom: 15px; font-size: 14px; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Iniciar Sesión</h2>
        {% if mensaje_error %}
            <div id="mensaje-error" class="alert">{{ mensaje_error }}</div>
        {% endif %}
        <form method="POST">
            <div class="form-group">
                <label>Usuario:</label>
                <input type="text" id="usuario" name="usuario" maxlength="50">
            </div>
            <div class="form-group">
                <label>Contraseña:</label>
                <input type="password" id="clave" name="clave">
            </div>
            <button type="submit" id="btn-ingresar">Ingresar</button>
        </form>
    </div>
</body>
</html>
"""

HTML_INVENTARIO = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Gestión de Productos</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f4f4f9; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; background: white; }
        th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
        th { background: #007bff; color: white; }
        .form-container { background: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
        .btn { padding: 8px 12px; color: white; border: none; border-radius: 4px; cursor: pointer; text-decoration: none; }
        .btn-crear { background: #28a745; }
        .btn-eliminar { background: #dc3545; }
        .alert { color: red; font-weight: bold; }
    </style>
</head>
<body>
    <h1 id="titulo-pagina">Gestión de Productos</h1>
    <a href="/logout" id="btn-salir">Cerrar Sesión</a>

    {% if mensaje_error %}
        <p id="alerta-error" class="alert">{{ mensaje_error }}</p>
    {% endif %}

    <div class="form-container">
        <h3>Registrar Nuevo Producto</h3>
        <form action="/crear" method="POST">
            <input type="text" id="nombre" name="nombre" placeholder="Nombre (máx 100 caracteres)" maxlength="100">
            <input type="text" id="categoria" name="categoria" placeholder="Categoría">
            <input type="number" step="0.01" id="precio" name="precio" placeholder="Precio ($)">
            <button type="submit" id="btn-guardar" class="btn btn-crear">Guardar Producto</button>
        </form>
    </div>

    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Categoría</th>
                <th>Precio</th>
                <th>Acción</th>
            </tr>
        </thead>
        <tbody id="tabla-productos">
            {% for prod in productos %}
            <tr>
                <td>{{ prod.id }}</td>
                <td>{{ prod.nombre }}</td>
                <td>{{ prod.categoria }}</td>
                <td>${{ "%.2f"|format(prod.precio) }}</td>
                <td>
                    <a href="/eliminar/{{ prod.id }}" id="btn-eliminar-{{ prod.id }}" class="btn btn-eliminar">Eliminar</a>
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        clave = request.form.get("clave", "").strip()
        
        if not usuario or not clave:
            error = "Campos obligatorios requeridos"
        elif len(usuario) > 50:
            error = "El usuario excede el límite de 50 caracteres"
        elif USUARIOS.get(usuario) == clave:
            session["usuario"] = usuario
            return redirect(url_for("inventario"))
        else:
            error = "Credenciales inválidas"
            
    return render_template_string(HTML_LOGIN, mensaje_error=error)

@app.route("/inventario")
def inventario():
    if "usuario" not in session:
        return redirect(url_for("login"))
    return render_template_string(HTML_INVENTARIO, productos=PRODUCTOS)

@app.route("/crear", methods=["POST"])
def crear():
    if "usuario" not in session:
        return redirect(url_for("login"))
    
    nombre = request.form.get("nombre", "").strip()
    categoria = request.form.get("categoria", "").strip()
    precio_raw = request.form.get("precio", "").strip()
    
    if not nombre or not categoria or not precio_raw:
        return render_template_string(HTML_INVENTARIO, productos=PRODUCTOS, mensaje_error="Todos los campos son obligatorios")
    
    try:
        precio = float(precio_raw)
        if precio <= 0:
            return render_template_string(HTML_INVENTARIO, productos=PRODUCTOS, mensaje_error="El precio debe ser un valor positivo")
    except ValueError:
        return render_template_string(HTML_INVENTARIO, productos=PRODUCTOS, mensaje_error="Precio no válido")

    nuevo_id = len(PRODUCTOS) + 1
    PRODUCTOS.append({"id": nuevo_id, "nombre": nombre, "categoria": categoria, "precio": precio})
    return redirect(url_for("inventario"))

@app.route("/eliminar/<int:item_id>")
def eliminar(item_id):
    global PRODUCTOS
    PRODUCTOS = [p for p in PRODUCTOS if p["id"] != item_id]
    return redirect(url_for("inventario"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(port=5000)