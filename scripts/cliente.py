import time
import rpyc
import sys
from random import randint

# Comentário para testar push do git 

# Questão 4 em diante
def criaVetor ():

    tamanho = int(input('Insira o tamanho do vetor: '))
    vetor = []
    
    for i in range(tamanho):
        vetor.append(randint(0, tamanho-1))
    return vetor


if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]
conn = rpyc.connect(server,18861)

# Questão 1
# print(conn.root)
# print(conn.root.get_answer())
# print(conn.root.the_real_answer_though)

clientVector = criaVetor()
# print(clientVector, sum(clientVector))

# Questões 5 em diante
start = time.time()

# Questão 4 em diante
sumVector = conn.root.vectorSum(clientVector)
print(f'A soma dos elementos do vetor é {sumVector}')

# Questões 5 em diante
end = time.time()
print(f'Tempo de resposta :{end-start}')


# Questão 3
# import rpyc 
# import sys 
# import os

# if len(sys.argv) < 2: 
#  exit("Usage {} SERVER".format(sys.argv[0])) 

# server = sys.argv[1] 
# conn = rpyc.connect(server,18861) 
# print(conn.get_question) 
