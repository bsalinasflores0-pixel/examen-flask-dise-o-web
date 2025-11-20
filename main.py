from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nombre = request.form.get("nombre", "")
        edad = int(request.form.get("edad", 0))
        cantidad = int(request.form.get("cantidad", 0))

        precio_tarro = 9000
        total_sin_desc = cantidad * precio_tarro

        if edad < 18:
            porcentaje_desc = 0
        elif edad <= 30:
            porcentaje_desc = 15
        else:
            porcentaje_desc = 25

        monto_desc = total_sin_desc * porcentaje_desc / 100
        total_con_desc = total_sin_desc - monto_desc

        return render_template(
            "ejercicio1.html",
            nombre=nombre,
            edad=edad,
            cantidad=cantidad,
            total_sin_desc=total_sin_desc,
            porcentaje_desc=porcentaje_desc,
            monto_desc=monto_desc,
            total_con_desc=total_con_desc
        )
    return render_template("ejercicio1.html")

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None

    if request.method == "POST":
        usuario = request.form.get("usuario", "")
        contrasena = request.form.get("contrasena", "")

        if usuario == "juan" and contrasena == "admin":
            mensaje = "Bienvenido Administrador juan"
        elif usuario == "pepe" and contrasena == "user":
            mensaje = "Bienvenido Usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("ejercicio2.html", mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)