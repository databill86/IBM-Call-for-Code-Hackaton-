import socket
import sys
import csv
import pickle
from time import sleep
import os
import random


def client():
    try:
#Me conecto al server el cual me enviara la data del csv
        s = socket.socket()         
        host = "127.0.0.1" 
        port = 2526               

        s.connect((host, port))
        data = pickle.loads( s.recv(1024)) # recivo la data para luego parsarla a un nuevo csv que se segenera automaticamente
        s.close ()

        numberF = random.randint(1,21)*5
        os.system("mkdir "+str(numberF))

        myFile = open(str(numberF)+'/data.csv', 'w')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(data)

            os.system("mv "+str(numberF)+" Data")

        print "csv received"
        sleep(9.0)# espero 11 segundos para que no vuelva a sobre escribir data o crear un archivo con la misma data
        
    except socket.error: #En caso de que este se conecte a otro wifi y este no tenga el server corriendo, evitara un error socket para seguir buscando las Pi-AP
    	pass



def detect_wifi(): #detecta si hay conexiones wifi.

    try:

	    myip=socket.gethostbyname(socket.gethostname())



    	    if myip == "127.0.0.1": # Si la IP es local y no tiene asignada una IP, este volvera a empezar el proceso de busca de wifi

    		    print "no wifi"

    	    else:
        	    print "found wifi" # Si la IP no es local, significara que ya un dhcp le asigno una dirrecion,lo que significa que esta conectado a una red wifi.
                

        	    client() #Cuando encuntre un wifi ejecuto la funcion client para buscar el csv en el server la la piAP y descargar el csv.

        	   



    except socket.gaierror: #cuando se decconecte de una conexion o seconecte, el script seguira coriendo.
    	pass
        
while True: #Se mantiene buscando wifi (Pi-Ap) constante mente 
	detect_wifi()
