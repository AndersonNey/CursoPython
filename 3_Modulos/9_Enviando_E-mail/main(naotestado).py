
from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart   #quem ta enviando , assunto da mensagem ,para quem
from email.mime.text import MIMEText             #recebe o corpo do email pode ser texto plan text ou um texto em html
from email.mime.image import MIMEImage           #vai receber uma imagem para anexar no email
import smtplib                                   #ele vai conectar no servidor smtp  ele que realmente vai mandar a mensagem em si

import os 
caminho = os.path.dirname(os.path.realpath(__file__))

meu_email = 'meu email'
minha_senha = '4545'

with open(caminho + r'\template.html','r',encoding="utf-8") as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y') 
    corpo_msg = template.substitute(nome='Carlos de Souza', data = data_atual)

msg = MIMEMultipart()
msg['from'] = 'seu nome'
msg['to'] = 'e-mail do cliente'  #e-mail do clinete
msg['subject'] = 'asunto do e-mail'


corpo = MIMEText(corpo_msg, 'html')   #como estou mandando um html eu preciso especificar       ,'html'
msg.attach(corpo)

with open(caminho + r'\imagem.jpg' , 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)


with smtplib.SMTP(host = 'smtp.gmail.com',port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email,minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso')
    except Exception as e:
        print('E-mail nao enviado...')
        print('Erro',e)
    























