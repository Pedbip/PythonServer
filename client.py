#-*- coding: utf8 -*-

import socket

SERVER_PORT = 8000

#criar o objeto socket cliente
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#conectar no servidor 
socket_cliente.connect(('localhost', SERVER_PORT))
print(f'conexao estabelecida com sucesso')

#envia ping para o servidor
socket_cliente.sendall(b'ping!')

#aguarda a resposta do servidor
dado = socket_cliente.recv(1024)
dado = dado.decode()

#debug
print(f'recebido do servidor: {dado}')

#encerrar conexao
socket_cliente.close()