#importando bibliotecas
import matplotlib.pyplot as plt
import numpy as np


def PartePar (entfcn):
    flp = np.flip(entfcn)
    evenpt = (entfcn+flp)/2
    return evenpt

def ParteImpar (entfcni):
    flp = np.flip(entfcni)
    oddpt = (entfcni-flp)/2
    return oddpt

def Plotar (t, f, ptp, pti):
    plt.title('Sinal')
    plt.subplot(412)
    plt.stem(t, f)
    plt.title('Parte Par')
    plt.subplot(413)
    plt.stem(t, ptp)
    plt.title('Parte Ímpar')
    plt.subplot(414)
    plt.stem(t, pti)
    plt.show()
    
 
tmp = np.arange(0,8)    
funcao = tmp**2
parpt = PartePar(funcao)
imparpt = ParteImpar(funcao)
#somapts = Soma()
print ('Sinal: '+ funcao,'\n')
print ('Parte par: '+ parpt,'\n')
print ('Parte impar: '+ imparpt,'\n')
#print ('Soma: ', somapts'\n')
i = input('Deseja plotar os graficos? (Y/N)?')
if (i=='Y'):
    Plotar(tmp, funcao, parpt, imparpt)



#oddSignal = 1/2*(array1[n]-array1[])




