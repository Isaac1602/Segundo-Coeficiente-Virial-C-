import numpy as pd
import matplotlib.pyplot as plt 

#Se agrega la ruta del archivo
ruta = 'Caso1_sigma/SegCoefVirSigma1.0Eps1.00e+00.dat'

# Read .dat file into a pandas DataFrame
tabla = pd.loadtxt(ruta)

Temperatuas = tabla[:, 0]  
BT = tabla[:, 1]  

plt.figure()
plt.plot(Temperatuas, BT, marker = 'o', linestyle = '-', color = 'r')
plt.title('Grafica del Segundo Coeficiente del Virial')
plt.xlabel('T*')
plt.ylabel('B(T*)*')
plt.grid(True)
plt.show()