import xmlrpclib, os
numLists = [ 1 , 2, 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10, 11, 12, 13, 14, 15];
for x in numLists:
    x = input("Ingrese un numero a la lista:  ")

s = xmlrpclib.ServerProxy('http://localhost:8001')