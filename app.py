from wtforms import StringField
from flask_wtf import FlaskForm
from flask import Flask, render_template, request, redirect, url_for, flash
import os
from forms import FormIndex, FormRecuperar, FormSubir, FormRegistro
import yagmail
import sqlite3
import sys

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/',methods=['GET', 'POST'])
def index():

    form = FormIndex()
    if request.method == "POST":
        usuario = form.usuario.data
        contraseña = form.contraseña.data
        with sqlite3.connect("redsocial.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM usuarios WHERE usuario=? AND contraseña=?", [usuario, contraseña])
            registro = cur.fetchone()
            if registro:
                if registro[8]:
                    return render_template('home.html')
                else:
                    flash('Usuario no activo')
                    return redirect('/')
            else:
                flash('Usuario o contraseña incorrectos')
                return redirect('/')

    return render_template('index.html', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('index.html')


@app.route('/registro',methods=['POST','GET'])
def registro():
    form = FormRegistro()
    if request.method == "POST":
        nombre = form.nombre.data
        apellido = form.apellido.data
        email = form.email.data
        fecha = request.form['fecha']
        usuario = form.usuario.data
        contraseña = form.contraseña.data
        sexo = request.form['sexo']
        try:
            with sqlite3.connect("redsocial.db") as con:
                cur = con.cursor() #manipula la conexión a la bd
                cur.execute("INSERT INTO usuarios VALUES (null,?,?,?,?,?,?,?,False)", (nombre,apellido,email,fecha,usuario,contraseña,sexo))
                con.commit()# confirma la transacción
            yag = yagmail.SMTP('imacol.misiontic@gmail.com','misiontic')
            yag.send(to=email, subject='Activa tu cuenta', contents = "Activa tu cuenta dando click <a href='http://localhost:5000/activar?usuario=" + usuario + "'> aqui</a>")
            flash('Por favor revise el correo para activar su cuenta')

            return redirect('/')
        except:
            con.rollback()
            return 'No se pudo guardar' + sys.exc_info()[1].args[0]

    return render_template('registrarse.html', form=form)


@app.route('/forgot',methods=['POST','GET'])
def forgot():

    form = FormRecuperar()

    if (form.validate_on_submit()):
        yag = yagmail.SMTP('imacol.misiontic@gmail.com','misiontic')
        yag.send(to=form.email.data, subject='Recupera tu cuenta', contents = 'Activa tu cuenta ('+ request.method +')')
        return redirect('/')
    return render_template('/recuperarcontrasena.html', form=form)
    
@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('home.html')


@app.route('/subir',methods=['POST','GET'])
def subir():
    form = FormSubir()

    if (form.validate_on_submit()):
        #En esta parte se guardará la imagen
        return redirect('/home')

    return render_template('subir.html', form=form)


@app.route('/perfil',methods=['GET','POST'])
def perfil():
    return render_template('profile.html')

@app.route('/activar')
def activar():
    usuario = request.args.get('usuario')
    try:
        with sqlite3.connect("redsocial.db") as con:
            cur = con.cursor() #manipula la conexión a la bd
            cur.execute("UPDATE usuarios SET activo=True WHERE usuario=?", [usuario])
            con.commit()# confirma la transacción
        flash('Usuario activado, ya puede ingresar sesion')
        return redirect('/')
    except:
        con.rollback()
        return 'No se pudo guardar' + sys.exc_info()[1].args[0]



if __name__=='__main__':
    app.run()