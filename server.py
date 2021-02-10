#!/usr/bin/env python3
import socket



SERVER_ADDRESS = '127.0.0.1'

SERVER_PORT = 22224

sock_listen = socket.socket()

sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))

sock_listen.listen(5)

print("Server in ascolto su %s." % str((SERVER_ADDRESS, SERVER_PORT)))#comunica che il server è attivo con le specifiche di indirizzo e porta


while True:
    sock_service, addr_client = sock_listen.accept()#accettà la richiesta di comunicazione e
    print("\nConnessione ricevuta da " + str(addr_client))# definisce l'indirizzo del client e che la comunicazione è avvenuta
    print("\nAspetto di ricevere i dati ")#finchè non riceve segnala che non sono avvenute iterazioni tra client e server
    contConn=0
    while True:
        dati = sock_service.recv(2048)
        contConn+=1
        if not dati:
            print("Fine dati dal client. Reset")#chiude e resetta cache dai dati inviati in caso di mancanza di dati non inviati
            break
        
        dati = dati.decode()#decodifica dati in arrivo
        print("Ricevuto: '%s'" % dati)#output dei dati in arrivo dal client
        if dati=='0':
            print("Chiudo la connessione con " + str(addr_client))#chiude la comunicazione con il client che comunica la chiusura del canale
            break
        dati = "Risposta a : " + str(addr_client) + ". Il valore del contatore è : " + str(contConn)#contatore delle comunicazioni avvenute con il client specifico(guardare indirizzo)

        dati = dati.encode()

        sock_service.send(dati)

    sock_service.close()