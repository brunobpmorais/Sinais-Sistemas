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

#-x[-n]
def reverseSignal(signal):
    xr = np.flip(signal)
    return xr

#sinal incial reverso
def reverseSignalStrt(signalbgn, signalend):
    reversestrt = np.arange(-signalend, -signalbgn+1)
    return reversestrt

#intervalo de toda a função
def genVector(startsignal, reversesignalstrt):
    genvector = np.arange(min(min(startsignal), min(reversesignalstrt)), max(max(startsignal), max(reversesignalstrt))+1)
    return genvector

#preenchendo com zeros
def zeroFill(signal, genvector, signalbgn, reversesignal):
    dif = abs(len(signal)-len(genvector))
    zeros = np.zeros(dif)
    if vetorgeral[0]==signalbgn:
        xrg = np.hstack((zeros, reversesignal))
    else:
        xrg = np.hstack((reversesignal, zeros))

    return xrg   

def flipZeros(xrg):
    xg = np.flip(xrg)
    return xg

#calcular partes par e impar segundo formula
def evenPt(xg, xrg):
    even = 0.5*(xg+xrg)
    return even

def oddPt(xg, xrg):
    odd= 0.5*(xg-xrg)
    return odd

#Definindo comprimento do sinal
comprimento = 20 #comprimento do sinal de entrada
tempoinicial = -3
sinal = calcSignal(comprimento)
sinalinicial = startSignal(sinal, tempoinicial)
iniciosinal = sinalinicial[0]
fimsinal = sinalinicial[comprimento-1]
xr = reverseSignal(sinal)
sinalinicialR = reverseSignalStrt(iniciosinal, fimsinal)
vetorgeral = genVector(sinalinicial, sinalinicialR)
vetorzeros = zeroFill(sinal, vetorgeral, iniciosinal, xr)
zeroreverso = flipZeros(vetorzeros)
par = evenPt(zeroreverso, vetorzeros)
impar = oddPt(zeroreverso, vetorzeros)

#funcoes de plot 

plt.title('Sinal')
plt.stem(vetorgeral, zeroreverso)
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