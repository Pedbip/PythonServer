# -*- coding> utf8 -*-

import socket

SERVER_ADRESS = '0.0.0.0'
SERVER_PORT = 8000

#Criando objeto socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#solicitar ao windows para ouvir na porta 8000
socket_servidor.bind((SERVER_ADRESS, SERVER_PORT))
socket_servidor.listen()

#aguardo uma conexao cliente
print(f'servidor ouvindo em {SERVER_ADRESS}:{SERVER_PORT} pronto para receber conexoes...')
socket_cliente, cliente_addr = socket_servidor.accept()

#debug
print(f'cliente conectado com sucesso., {cliente_addr[0]}:{cliente_addr[1]}')

#receber dados cliente 
dado_recebido = socket_cliente.recv(1024)
dado_recebido = dado_recebido.decode()

#debug
print(f'o cliente enviou: {dado_recebido}')

#responder para cliente
socket_cliente.sendall(b'pong!')



#encerrar conexao
socket_cliente.close()
