from SimpleXMLRPCServer import SimpleXMLRPCServer
#from xmlrpc.server import SimpleXMLRPCServer

class functions:
    def invertList(self, archive):
        file_object  = open("archivo.txt", "r")
        l1=file_object.readlines()
        l2 = l1.reverse()
        f = open("resultado1.txt","w+")
        for i in l2:            
            f.write( str(i) + "\r\n")    
        f.close()
        return 1

        return p+q
    def repeatNum(self, archive):
        file_object  = open(archive, "r")
        l1=file_object.readlines()
        numrepeat = 0
        actual = 0
        for i in l1:
            actual = numinList(i,l1)
            if actual > numrepeat:
                numrepeat = actual
        return numrepeat
    
    def numinList(self,num, List):
        result = 0
        for i in List:
            if i == num:
                result += 1
        return result


server = SimpleXMLRPCServer(("localhost", 8001))
server.register_instance(functions())
print("Servidor funcionando en el puerto 8001")
server.serve_forever()