import logging
import cx_Oracle
import socket

def konekcija():
    serverSocket = socket.socket()
    localHost = "127.0.0.1"
    port = 10003

    try:
        serverSocket.bind((localHost, port))
    except socket.error as e:
        print(str(e))

    print("Waiting for a connection...")
    serverSocket.listen(5)

    client, address = serverSocket.accept()
    print("Connect to: " + address[0] + ":" + str(address[1]))

    poruka = client.recv(2048)
    poruka=poruka.decode("utf-8")


    id=((poruka.split('\n')[1]).split(':')[1]).split(' ')[0]
    potrosnja=((poruka.split('\n')[2]).split(':')[1]).split(' ')[0]
    mesec=((poruka.split(' ')[3]).split(':')[1]).split(' ')[0]

    upisUBazu(id,potrosnja,mesec)
    print("Server primio poruku od klijenta " + poruka)

    serverSocket.close()

def konekcijaKaBazi():
    con = cx_Oracle.connect('bp1/ftn@localhost')
    return con

def IdPotrosnje():
    con=konekcijaKaBazi()
    sqlquery="select count(*) from POTROSNJA"
    cursor = con.cursor()
    n=cursor.execute(sqlquery)
    return n

def upisUBazu(id,potrosnja,mesec):
    con=konekcijaKaBazi()
    br=IdPotrosnje()
    br+=1
    sqlquery="insert into POTROSNJA values ("+br+","+id+","+potrosnja+","+mesec+")"
    cursor = con.cursor()
    cursor.execute(sqlquery)


konekcija()