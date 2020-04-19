from luckapp import app
from flask_mail import Message

def RegistrationMessage(data):
    message_body =  f"Olá {data['full_name']}, seja muito bem-vindo! Esse é um email de confirmação de cadastro na plataforma LuckApp, fique ligado para mais informaçōes."

    return Message(subject='Confirmação de cadastro - LuckApp',
            sender=app.config.get("MAIL_USERNAME"),
            recipients=[data['email']],
            body=message_body)

def CreateMessage(data, type):
    if type == 'registration_email':
        return RegistrationMessage(data)
    else:
        return Message(subject=data['subject'],
            sender=app.config.get("MAIL_USERNAME"),
            recipients=data['recipients'],
            body=data['body'])
