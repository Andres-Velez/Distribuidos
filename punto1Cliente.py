import xmlrpclib, os

f = open("archivo.txt","w+")
for i in range(15):
    num = input("Ingrese un numero a la lista:  ")
    f.write( str(num) + "\r\n")    
f.close()

typeoperation = input("Ingrese 1 para invertir la lista o 2 para mostrar el numero mas repetido en ella:  ")


s = xmlrpclib.ServerProxy('http://localhost:8001')
if typeoperation == 1:
    str(s.invertList("archivo.txt"))
    print('terminado')
if typeoperation == 2:
    print("El numero que mas se repite es" + str(s.repeatNum("archivo.txt")))