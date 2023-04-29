import rpyc
import sys
from random import randint

def criaVetor ():

    tamanho = int(input('Insira o tamanho do vetor: '))
    vetor = []
    
    for i in range(tamanho):
        vetor.append(randint(0, tamanho))
    return vetor


if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]
conn = rpyc.connect(server,18861)

print(conn.root)
print(conn.root.get_answer())
print(conn.root.the_real_answer_though)

clientVector = criaVetor()
# print(clientVector, sum(clientVector))
sumVector = conn.root.vectorSum(clientVector)
print(sumVector)


# Questão 3
# import rpyc 
# import sys 
# import os

# if len(sys.argv) < 2: 
#  exit("Usage {} SERVER".format(sys.argv[0])) 

# server = sys.argv[1] 
# conn = rpyc.connect(server,18861) 
# print(conn.get_question) 
