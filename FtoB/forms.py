#criar os formularios
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from FtoB.models import Usuario

class FormLogin(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField(label="Entrar") #deixei assim pra testar

class FormCriarConta(FlaskForm):
    email =  StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Nome de Usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6,20)])
    confirmar_senha =  PasswordField("Confirme a Senha",validators=[DataRequired(), EqualTo('senha')])
    botao_confirmacao = SubmitField("Criar conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if  usuario:
            return ValidationError("Email ja cadastrado, faça login para continuar")