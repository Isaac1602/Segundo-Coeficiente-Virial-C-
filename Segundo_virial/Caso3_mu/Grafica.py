import numpy as pd
import matplotlib.pyplot as plt 

#Se agrega la ruta del archivo
ruta1 = 'SegCoefVirSigma1.0Eps1.0Mu1.00e+00.dat'
ruta2 = 'SegCoefVirSigma1.0Eps1.0Mu2.00e-01.dat'
ruta3 = 'SegCoefVirSigma1.0Eps1.0Mu4.00e-01.dat'
ruta4 = 'SegCoefVirSigma1.0Eps1.0Mu6.00e-01.dat'
ruta5 = 'SegCoefVirSigma1.0Eps1.0Mu8.00e-01.dat'
# Read .dat file into a pandas DataFrame

tabla1 = pd.loadtxt(ruta1)
tabla2 = pd.loadtxt(ruta2)
tabla3 = pd.loadtxt(ruta3)
tabla4 = pd.loadtxt(ruta4)
tabla5 = pd.loadtxt(ruta5)

Temperatuas = tabla1[:, 0]  

BT1 = tabla1[:, 1]  
BT2 = tabla2[:, 1]  
BT3 = tabla3[:, 1]  
BT4 = tabla4[:, 1]  
BT5 = tabla5[:, 1]  

plt.figure()
plt.plot(Temperatuas, BT1, marker = 'o', linestyle = '-', label = 'Mu 1.0')
plt.plot(Temperatuas, BT2, marker = 'o', linestyle = '-', label = 'Mu 0.2')
plt.plot(Temperatuas, BT3, marker = 'o', linestyle = '-', label = 'Mu 0.4')
plt.plot(Temperatuas, BT4, marker = 'o', linestyle = '-', label = 'Mu 0.6')
plt.plot(Temperatuas, BT5, marker = 'o', linestyle = '-', label = 'Mu 0.8')
plt.title('Grafica del Segundo Coeficiente del Virial')
plt.xlabel('T*')
plt.ylabel('B(T*)*')
plt.legend()
plt.grid(True)
plt.show()