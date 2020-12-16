#Formularios

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, InputRequired

class FormIndex(FlaskForm):
    usuario =  StringField('Usuario',validators=[DataRequired('No dejar vacío, completar')], render_kw={"placeholder": "Nombre de usuario o correo electrónico"})
    contraseña = PasswordField('Contraseña',validators=[DataRequired('No dejar vacío, completar')], render_kw={"placeholder": "Contraseña"}, id="password")
    enviar = SubmitField('Iniciar sesión')

class FormRecuperar(FlaskForm):
    email = StringField('Email',validators=[DataRequired('No dejar vacío, completar')], render_kw={"placeholder": "Correo de verificación"})
    enviar = SubmitField('Enviar correo')

class FormSubir(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired('No dejar vacío, completar')], render_kw={"placeholder": "Nombre de la imagen"})
    tags = StringField('Tags',validators=[DataRequired('No dejar vacío, completar')], render_kw={"placeholder": "Tags de la imagen"})
    esPublica = BooleanField('esPublica')
    enviar = SubmitField('Subir')

class FormRegistro(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired('No dejar vacío, completar')], render_kw={"placeholder": "Nombres"})
    apellido = StringField('Apellido', validators=[DataRequired('No dejar vacío, completar')], render_kw={"placeholder": "Apellidos"})
    email = StringField('Email', validators=[DataRequired('No de jar vacío, completar')], render_kw={"placeholder": "Correo electrónico"})
    usuario = StringField('Usuario', validators=[DataRequired('No dejar vacío, completar')], render_kw={"placeholder": "Usuario"})
    contraseña = PasswordField('Contraseña', validators=[DataRequired('No dejar vacío, completar')], render_kw={"placeholder": "Contraseña"})
    enviar = SubmitField('Registrarse')

class FormActualizar(FlaskForm):

    nombre = StringField('Nombre', validators=[DataRequired('No dejar vacío, completar')], render_kw={"placeholder": "Nombres"})
    apellido = StringField('Apellido', validators=[DataRequired('No dejar vacío, completar')], render_kw={"placeholder": "Apellidos"})
    email = StringField('Email', validators=[DataRequired('No de jar vacío, completar')], render_kw={"placeholder": "Correo electrónico"})
    usuario = StringField('Usuario', validators=[DataRequired('No dejar vacío, completar')], render_kw={"placeholder": "Usuario"})
    enviar = SubmitField('Actualizar')
