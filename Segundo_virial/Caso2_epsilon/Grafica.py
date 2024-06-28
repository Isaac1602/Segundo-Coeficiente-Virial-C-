import numpy as pd
import matplotlib.pyplot as plt 

#Se agrega la ruta del archivo
ruta1 = 'SegCoefVirEps1.0Sig1.00e+00.dat'
ruta2 = 'SegCoefVirEps1.0Sig1.50e+00.dat'
ruta3 = 'SegCoefVirEps1.0Sig5.00e-01.dat'
# Read .dat file into a pandas DataFrame

tabla1 = pd.loadtxt(ruta1)
tabla2 = pd.loadtxt(ruta2)
tabla3 = pd.loadtxt(ruta3)

Temperatuas = tabla1[:, 0]  

BT1 = tabla1[:, 1]  
BT2 = tabla2[:, 1]  
BT3 = tabla3[:, 1]  

plt.figure()
plt.plot(Temperatuas, BT1, marker = 'o', linestyle = '-', color = 'r', label = 'Sigma 1.0')
plt.plot(Temperatuas, BT2, marker = 'o', linestyle = '-', color = 'b', label = 'Sigma 1.5')
plt.plot(Temperatuas, BT3, marker = 'o', linestyle = '-', color = 'g', label = 'Sigma 0.5')
plt.title('Grafica del Segundo Coeficiente del Virial')
plt.xlabel('T*')
plt.ylabel('B(T*)*')
plt.legend()
plt.grid(True)
plt.show()