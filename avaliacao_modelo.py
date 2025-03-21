# Matriz Confusão 

import numpy as np

VP = 2084
FP = 115
VN = 3254
FN = 245

matriz_confusao = np.array([[VP, FP], [FN, VN]])

def sensibilidade(matriz_confusao):
    return matriz_confusao[0][0] / (matriz_confusao[0][0] + matriz_confusao[0][1])

print(sensibilidade(matriz_confusao))

def especificidade(matriz_confusao):
    return matriz_confusao[1][1] / (matriz_confusao[1][0] + matriz_confusao[1][1])

print(especificidade(matriz_confusao))

def acuracia(matriz_confusao):
    return (matriz_confusao[0][0] + matriz_confusao[1][1]) / np.sum(matriz_confusao)

print(acuracia(matriz_confusao))

def precisao(matriz_confusao): 
    return matriz_confusao[0][0] / (matriz_confusao[0][0] + matriz_confusao[1][0])

print(precisao(matriz_confusao))

def f_score(matriz_confusao):
    return 2 * (precisao(matriz_confusao) * sensibilidade(matriz_confusao)) / (precisao(matriz_confusao) + sensibilidade(matriz_confusao))

print(f_score(matriz_confusao))