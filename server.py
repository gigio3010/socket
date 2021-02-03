
#!/usr/bin/env python3
#https://realpython.com/python-sockets/
import socket

HOST = '127.0.0.1'  # Indirizzo dell'interfaccia standard di loopback (localhost)
PORT = 65432        # Porta di ascolto, la lista di quelle utilizzabili parte da >1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("[*] In ascolto su %s:%d" % (HOST, PORT))
    clientsocket, address = s.accept()
    with clientsocket as cs:
        print('Connessione da', address)
        while True:
            data = cs.recv(1024)
            if not data:
                break
            cs.sendall(data)