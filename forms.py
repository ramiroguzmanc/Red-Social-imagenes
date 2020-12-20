#Formularios

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length
from wtforms.fields.html5 import EmailField

class FormIndex(FlaskForm):
    usuario =  StringField('Usuario',validators=[DataRequired('No dejar vacío, completar'),Length(min=6,max=25)], render_kw={"placeholder": "Nombre de usuario"})
    contraseña = PasswordField('Contraseña',validators=[DataRequired('No dejar vacío, completar'),Length(min=6,max=30)], render_kw={"placeholder": "Contraseña"}, id="password")
    enviar = SubmitField('Iniciar sesión')

class FormRecuperar(FlaskForm):
    usuario = StringField('Usuario',validators=[DataRequired('No dejar vacío, completar'),Length(min=10,max=40)], render_kw={"placeholder": "Usuario registrado"})
    enviar = SubmitField('Enviar correo')

class FormSubir(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired('No dejar vacío, completar'),Length(min=3,max=25)], render_kw={"placeholder": "Nombre de la imagen"})
    tags = StringField('Tags',validators=[DataRequired('No dejar vacío, completar'),Length(min=3,max=25)], render_kw={"placeholder": "Tags de la imagen"})
    esPublica = BooleanField('esPublica')
    enviar = SubmitField('Subir')

class FormRegistro(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired('No dejar vacío, completar'),Length(min=3,max=25)], render_kw={"placeholder": "Nombres"})
    apellido = StringField('Apellido', validators=[DataRequired('No dejar vacío, completar'),Length(min=2,max=25)], render_kw={"placeholder": "Apellidos"})
    email = EmailField('Email', validators=[DataRequired('No de jar vacío, completar'),Length(min=10,max=40)], render_kw={"placeholder": "Correo electrónico"})
    usuario = StringField('Usuario', validators=[DataRequired('No dejar vacío, completar'),Length(min=6,max=25)], render_kw={"placeholder": "Usuario"})
    contraseña = PasswordField('Contraseña', validators=[DataRequired('No dejar vacío, completar'),Length(min=6,max=30)], render_kw={"placeholder": "Contraseña"})
    enviar = SubmitField('Registrarse')

class FormActualizar(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired('No dejar vacío, completar'),Length(min=3,max=25)], render_kw={"placeholder": "Nombres"})
    apellido = StringField('Apellido', validators=[DataRequired('No dejar vacío, completar'),Length(min=2,max=25)], render_kw={"placeholder": "Apellidos"})
    email = EmailField('Email', validators=[DataRequired('No dejar vacío, completar'),Length(min=10,max=40)], render_kw={"placeholder": "Correo electrónico"})
    usuario = StringField('Usuario', validators=[DataRequired('No dejar vacío, completar'),Length(min=6,max=25)], render_kw={"placeholder": "Usuario"})
    enviar = SubmitField('Actualizar')

class Formcambiar(FlaskForm):
    contraseña = PasswordField('Contraseña', validators=[DataRequired('No dejar vacío, completar'),Length(min=6,max=30)], render_kw={"placeholder": "Nueva contraseña"})
    enviar = SubmitField('Cambiar contraseña')
