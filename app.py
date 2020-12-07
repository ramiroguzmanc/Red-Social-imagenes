from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/recuperarcontrasena")
def recuperarcontrasena():
	return render_template("recuperarcontrasena.html")

@app.route("/registro")
def registro():
	return render_template("registrarse.html")

@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/subir")
def subir():
	return render_template("subir.html")

@app.route("/perfil")
def perfil():
	return render_template("profile.html")

