import rpyc

class MyService(rpyc.Service):

    def on_connect(self, conn):
        print("Você está conectado ao Servidor!")

    def on_disconnect(self, conn):
        print("Você perdeu a conexão com o Servidor...")


    def exposed_get_answer(self): # este é um método exposto
        return 42
    
    exposed_the_real_answer_though = 43 # este é um atributo exposto
    
    def get_question(self): # este método não é exposto
        return "Qual é a cor do cavalo branco de Napoleão?"
    
    def exposed_vectorSum(self, vector):
        return sum(vector)

#Para iniciar o servidor
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()