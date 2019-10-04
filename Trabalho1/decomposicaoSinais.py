#importando bibliotecas
import matplotlib.pyplot as plt
import numpy as np
import math as mt

#Definindo o comprimento do sinal e sinal
def calcSignal(lenght):
    tmp = np.arange(lenght)    
    signal = tmp**2
    return signal

def startSignal(signal, starttime):
    lensignal = len(signal)
    #sinal inicial
    startsignal = np.arange(starttime, starttime+lensignal, 1)
    return startsignal

#Definindo comprimento do sinal
comprimento = 20 #comprimento do sinal de entrada
tempoinicial = -3
sinal = calcSignal(comprimento)
sinalinicial = startSignal(sinal, tempoinicial)

#-x[-n]
xr = np.flip(sinal)
sinalinicialR = np.arange(-fimsinal, -iniciosinal+1)

#intervalo de toda a função
vetorgeral = np.arange(min(min(sinalinicial), min(sinalinicialR)), max(max(sinalinicial), max(sinalinicialR))+1)
lengeral = len(vetorgeral)

#preenchendo com zeros
dif = abs(lensinal-lengeral)
zeros = np.zeros(dif)
if vetorgeral[0]==iniciosinal:
    xrg = np.hstack((zeros, xr))
else:
    xrg = np.hstack((xr, zeros))
    
xg = np.flip(xrg)

#calcular partes par e impar segundo formula
par = 0.5*(xg+xrg)
impar= 0.5*(xg-xrg)

#funcoes de plot 

plt.title('Sinal')
plt.stem(vetorgeral, xg)
plt.show()

plt.title('Parte Par')
plt.stem(vetorgeral, par)
plt.show()

plt.title('Parte Ímpar')
plt.stem(vetorgeral, impar)
plt.show()

plt.title('Soma de Partes Par e Ímpar')
plt.stem(vetorgeral, par+impar)
plt.show()