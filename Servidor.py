from SimpleXMLRPCServer import SimpleXMLRPCServer
#from xmlrpc.server import SimpleXMLRPCServer

class functions:

    def Verification(self, user, password):
        if(user == "falcao" and password == "galatsatay2020"):
            return 1
        else:
            return 0

    def invttruelist(self, lista,lista2):
        f = open("resultado1.txt","w+")
        if not lista == []:
            f.write( lista[-1] + "\r\n")
            lista2.append(lista[-1])
            lista.pop(-1)
            self.invttruelist( lista, lista2)
        f.close()
        return lista2
            
    def invertList(self, archive):
        file_object  = open("archivo.txt", "r")
        l1=file_object.readlines()
        l2 = []
        print(self.invttruelist(l1,l2))
        return 1

    def numinList(self,num, List):
        result = 0
        for i in List:
            if i == num:
                result += 1
        return result

    def repeatNum(self, archive):
        
        file_object  = open(archive, "r")
        l1=file_object.readlines()
        self.numinList(1,l1)
        """
        numrepeat = 0
        actual = 0
        for i in l1:
            actual = self.numinList(i,l1)
            if actual > numrepeat:
                numrepeat = actual
        return numrepeat
        """
    
    


server = SimpleXMLRPCServer(("localhost", 8001))
server.register_instance(functions())
print("Servidor funcionando en el puerto 8001")
server.serve_forever()