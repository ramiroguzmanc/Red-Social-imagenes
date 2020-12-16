from wtforms import StringField
from flask_wtf import FlaskForm
from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
from forms import FormIndex, FormRecuperar, FormSubir, FormRegistro
import yagmail
import sqlite3
import sys
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/',methods=['GET', 'POST'])
def index():

    form = FormIndex()
    if request.method == "POST":
        usuario = form.usuario.data
        contraseña = form.contraseña.data
        with sqlite3.connect("redsocial.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM usuarios WHERE usuario=?", [usuario])
            registro = cur.fetchone()
            if registro:
                if registro[8]:
                    if check_password_hash(registro[6], contraseña):
                        session.clear()
                        session["usuario"] = registro[5]
                        session["id"] = registro[0]
                        return render_template('home.html')
                    else:
                        flash('Usuario o contraseña incorrectos')
                        return redirect('/')
                else:
                    flash('Usuario no activo')
                    return redirect('/')
            else:
                flash('Usuario no registrado')
            

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
        contraseña = generate_password_hash(form.contraseña.data)
        sexo = request.form['sexo']
        try:
            with sqlite3.connect("redsocial.db") as con:
                cur = con.cursor() #manipula la conexión a la bd
                cur.execute("INSERT INTO usuarios VALUES (null,?,?,?,?,?,?,?,False,'usuario')", (nombre,apellido,email,fecha,usuario,contraseña,sexo))
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
    if request.method == "POST":
        if 'imagen' not in request.files:
            flash('No hay parte de archivo')
            return redirect('/subir')
        f = request.files['imagen']
        if f.filename == '':
            flash('Archivo no seleccionado')
            return redirect('/subir')

        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        propietario_id = session["id"]
        nombre = form.nombre.data
        tags = form.tags.data
        archivo = str(filename)
        restriccion = form.esPublica.data
        try:
            with sqlite3.connect("redsocial.db") as con:
                cur = con.cursor() #manipula la conexión a la bd
                cur.execute("INSERT INTO imagenes VALUES (null,?,?,?,?,?)", (propietario_id,nombre,tags,archivo,restriccion))
                con.commit()# confirma la transacción
            return redirect('/home')
        except:
            con.rollback()
            return 'No se pudo guardar' + sys.exc_info()[1].args[0]
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