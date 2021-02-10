#!/usr/bin/env python3


input_string = 'Hello'
print(type(input_string))
input_bytes_encoded = input_string.encode()
print(type(input_bytes_encoded))
print(input_bytes_encoded)
output_string=input_bytes_encoded.decode()
print(type(output_string))
print(output_string)

import socket #importazione degli elementi e funzioni socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224

sock_service = socket.socket()#definizione socket efunzione

sock_service.connect((SERVER_ADDRESS, SERVER_PORT))#permette di comunicare col server attravero le variabili di indirizzo e porta a livello IPC

print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT)))
while True:#while che gestische le opzioni confrontando il valore scritto con le variabili presenti nei casi di esso
    try:
        dati = input("Inserisci i dati da inviare (0 per terminare la connessione): ")
    except EOFError:
        print("\nOkay. Exit")
        break
     # if not dati: #esso avvisa che se il set è vuoto di scrivere qualcosa perchè non gli permette di comunicare e permette di rieseguire l'iterazione con il server 
     #   print("Non puoi inviare una stringa vuota!")
     #   continue
    if not dati:#esso avvisa che se il set è vuoto di scrivere, chiude la comunicazione e interrope il funzionamento 
        print("Server non risponde. Exit")
        break
    if dati == '0':#chiude la comunicazione e interrompe il servizio
        print("Chiudo la connessione con il server!")
        break
    
    dati = dati.encode()

    sock_service.send(dati)

    dati = sock_service.recv(2048)

    #if not dati: #dovrebbe permettere di uscire dal collegamento
    #    print("Server non risponde. Exit")
     #   break
    
    dati = dati.decode()

    print("Ricevuto dal server:")#esegue il calcolo di iterazioni con il server come se fosse un contatore
    print(dati + '\n')

sock_service.close()