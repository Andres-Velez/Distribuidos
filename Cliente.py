import xmlrpclib, os

user = raw_input("Ingrese el usuario:  ")
password = raw_input("Ingrese la contrasenia:  ")
s = xmlrpclib.ServerProxy('http://localhost:8001')

if s.Verification(user, password) == 1:
    f = open("archivo.txt","w+")
    for i in range(15):
        num = input("Ingrese un numero a la lista:  ")
        f.write( str(num) + "\r\n")    
    f.close()

    typeoperation = input("Ingrese 1 para invertir la lista o 2 para mostrar el numero mas repetido en ella:  ")

    if typeoperation == 1:
        s.invertList("archivo.txt")
        print('terminado')
    if typeoperation == 2:
        print("El numero que mas se repite es" + str(s.repeatNum("archivo.txt")))
else :
    print("Usuario o contrasenia incorrecto")


