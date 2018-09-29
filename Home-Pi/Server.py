#!/usr/bin/python           
import pickle
import socket               
import csv

result =[]

with open('data.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        result.append(row)

s = socket.socket()         
host = "127.0.0.1" 
port = 2526                
s.bind((host, port))        

s.listen(5)                 
while True:
   c, addr = s.accept()     
   print 'Got connection from', addr
   Marray=pickle.dumps(result)
   c.send(Marray)
   c.close()            
