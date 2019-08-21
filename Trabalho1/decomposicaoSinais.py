#importando bibliotecas
import matplotlib.pyplot as plt
import numpy as np

def EvenSignal (funcao):
    flp = np.flip(funcao)
    evenpt = (funcao+flp)/2
    return evenpt

def OddSignal (funcao):
    flp = np.flip(funcao)
    oddpt = (funcao-flp)/2
    return oddpt


#funcoes
x = np.arange(0, 8)
funcao = 2*x**2
print(x)
print(funcao)
evenpt = EvenSignal()

plt.title('Sinal')
plt.subplot(412)
plt.stem(x, funcao)
plt.title('Parte Par')
plt.subplot(413)
plt.stem(x, EvenSignal())
plt.title('Parte Ímpar')
plt.subplot(414)
plt.stem(x, OddSignal())
plt.show()
    

#oddSignal = 1/2*(array1[n]-array1[])




