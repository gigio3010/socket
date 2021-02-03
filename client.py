#!/usr/bin/env python3

import socket

SERVER_ADDRESS = '127.0.0.1'  # The server's hostname or IP address
SERVER_PORT = 65433        # The port used by the server
sock_service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_service.connect((SERVER_ADDRESS, SERVER_PORT))
dati = input("Inserisci messaggio per il server: ")
dati = dati.encode()
# Invia i dati al server
sock_service.send(dati)
# Riceve i dati dal server
dati = sock_service.recv(2048)
if dati:
    # Converte i dati dal formato  byte a stringa
    dati = dati.decode()
    print("Ho ricevuto dal server: ")
    print(dati + '\n')
