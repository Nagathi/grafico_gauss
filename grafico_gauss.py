import numpy as np
import matplotlib.pyplot as plt
import math

listSoja = [196, 1375.1, 23, 12.9, 12.8, 2230.8, 3526, 12851, 3285.6, 2719.8, 7.6, 6838, 35885.7, 
            11431.2, 13723.2, 292, 7021.7, 4299.4, 19880.1, 2363.9, 20787.5] 

#Dados de produção de soja de todos os estados

listMilho = [90, 1079.1, 91.9, 23.2, 1.2, 1114.7, 1115.6, 2348.1, 2096, 458, 27.7, 49.6, 141, 172.9, 
            687.6, 2404.5, 33243.9, 6429, 8431, 366.2, 6085.8, 33.3, 3.2, 3270.8, 9614.2, 1980.4, 4390.1] 

#Dados de produção de milho de todos os estados

media1 = (np.average(listSoja))
media2 = (np.average(listMilho))

sigma1 = (np.std(listSoja))
sigma1 = round(sigma1)

sigma2 = (np.std(listMilho))
sigma2 = round(sigma2)

print(media1)
print(sigma1)

print(media2)
print(sigma2)

x = np.linspace(-50000, 50000)
soja = (1.0/(sigma1*np.sqrt(2.0*math.pi)))*np.exp(-0.5*((x-media1)/sigma1)**2.0)
milho = (1.0/(sigma2*np.sqrt(2.0*math.pi)))*np.exp(-0.5*((x-media2)/sigma2)**2.0)

plt.plot(x,soja,label=r'$\sigma$ Soja='+str(sigma1))
plt.plot(x,milho,label=r'$\sigma$ Milho='+str(sigma2))

plt.xlabel('Milhares de Toneladas')
plt.ylabel('Densidade')
plt.legend()
plt.tight_layout()
plt.show()