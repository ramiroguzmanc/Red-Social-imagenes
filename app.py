from flask import Flask, render_template, flash, request, redirect, url_for
import yagmail as yagmail


app = Flask(__name__)



@app.route('/',methods=['GET'])
def index():
    error = None

    try:
        if request.method == 'POST':
            username = request.form['usuario']
            password = request.form['password']

        else:
            username = request.args.get('usuario')
            password = request.args.get('password')

        if (username=="prueba" and password=="prueba1234"):
            return redirect('/home')
        else:
            if (username == None and password == None):
                error = "Escriba su clave y usuario"
                flash(error)
                return render_template('index.html')
            else:
                error = "Clave o contraseña invalidos"
                flash(error)
                return render_template('index.html')

    except:
        return render_template('index.html') 
    return render_template('index.html') 


@app.route('/login', methods=['GET'])
def login():
    return render_template('index.html')


@app.route('/registro',methods=['GET'])
def registro():
    return render_template('registrarse.html')


@app.route('/forgot',methods=['POST','GET'])
def forgot():
    error = None

    try:
        if request.method == 'POST':
            email = request.form['email']


        else:
            email = request.args.get('email')


        if (email!=None):
            yag = yagmail.SMTP('imacol.misiontic@gmail.com','misiontic')
            yag.send(to=email, subject='Activa tu cuenta', contents = 'Activa tu cuenta ('+ request.method +')')
            return redirect('/')
        else:
            return render_template('/recuperarcontrasena.html')
                

    except:
        return render_template('/recuperarcontrasena.html') 
    return render_template('/recuperarcontrasena.html')



@app.route('/home',methods=['GET'])
def gallery():
    return render_template('home.html')


@app.route('/subir',methods=['GET'])
def subir():
    return render_template('subir.html')

@app.route('/perfil',methods=['GET'])
def perfil():
    return render_template('profile.html')


if __name__=='__main__':
    app.run()