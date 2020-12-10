from wtforms import StringField
from flask_wtf import FlaskForm
from flask import Flask, render_template, request, redirect, url_for, flash
import os
from forms import FormIndex, FormRecuperar, FormSubir, FormRegistro
import yagmail

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/',methods=['GET', 'POST'])
def index():

    form = FormIndex()
    if(form.validate_on_submit()):
        if form.usuario.data=='prueba' and form.contraseña.data=='prueba1234':
            return redirect('/home')
    return render_template('index.html', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('index.html')


@app.route('/registro',methods=['POST','GET'])
def registro():
    form = FormRegistro()
    if(form.validate_on_submit()):
        yag = yagmail.SMTP('imacol.misiontic@gmail.com','misiontic')
        yag.send(to=form.email.data, subject='Activa tu cuenta', contents = 'Activa tu cuenta ('+ request.method +')')
        #En esta parte se guardará el usuario en la base de datos
        return redirect('/')


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
        yag = yagmail.SMTP('imacol.misiontic@gmail.com','misiontic')
        yag.send(to='jpsuarezr551@gmail.com', subject='Recupera tu cuenta', contents = 'Activa tu cuenta ('+ request.method +')')
        return redirect('/home')

    return render_template('subir.html', form=form)


@app.route('/perfil',methods=['GET','POST'])
def perfil():
    return render_template('profile.html')


if __name__=='__main__':
    app.run()