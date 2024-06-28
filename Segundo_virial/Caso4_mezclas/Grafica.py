import numpy as pd
import matplotlib.pyplot as plt 

#Se agrega la ruta del archivo
ruta1 = 'SegCoefVirSig10Eps10Con3.00e-01.dat'
ruta2 = 'SegCoefVirSig10Eps10Con5.00e-01.dat'
ruta3 = 'SegCoefVirSig10Eps10Con7.00e-01.dat'
# Read .dat file into a pandas DataFrame

tabla1 = pd.loadtxt(ruta1)
tabla2 = pd.loadtxt(ruta2)
tabla3 = pd.loadtxt(ruta3)

Temperatuas = tabla1[:, 0]  

BT1 = tabla1[:, 1]  
BT2 = tabla2[:, 1]  
BT3 = tabla3[:, 1]  

plt.figure()
plt.plot(Temperatuas, BT1, marker = 'o', linestyle = '-', color = 'r', label = 'Concentracion 0.3')
plt.plot(Temperatuas, BT2, marker = 'o', linestyle = '-', color = 'b', label = 'Concentracion 0.5')
plt.plot(Temperatuas, BT3, marker = 'o', linestyle = '-', color = 'g', label = 'Concentracion 0.7')
plt.title('Grafica del Segundo Coeficiente del Virial')
plt.xlabel('T*')
plt.ylabel('B(T*)*')
plt.legend()
plt.grid(True)
plt.show()