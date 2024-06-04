from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from PIL import Image, ImageDraw
from hashlib import sha256
import os

@shared_task
def cria_convite(nome, email):
    """Função para abrir a imagem padrão criar uma copia e escrever o nome do usuário e devolver essa copia"""
    template = os.path.join(settings.STATIC_ROOT, 'img/convite_fundo.png')

    imagem = Image.open(template)
    escrever_imagem = ImageDraw.Draw(imagem)
    escrever_imagem.text((30, 170), nome, fill=(200, 89, 255))

    chave_secreta = 'QUJIAUSHFU4589354aavvrsetg@%#$#11asf'
    token = sha256((email + chave_secreta).encode()).hexdigest()

    path_salvar = os.path.join(settings.MEDIA_ROOT, f'convites/{token}.png')
    imagem.save(path_salvar)
    # rodar no terminal -> python3 manage.py collectstatic

    # send_mail(assunto, mensagem, de qual e-mail?, para qual e-mail?)
    # send_mail('CADASTRO CONFIRMADO', f'Seu cadastro foi confirmado com sucesso. \n Aqui está o link do seu convite: http://127.0.0.1:8000/media/convites/{token}.png', 'de qual email?', recipient_list=[email])

    # Habilitar o Worker
    # -> celery -A projeto_celery worker --loglevel=INFO
