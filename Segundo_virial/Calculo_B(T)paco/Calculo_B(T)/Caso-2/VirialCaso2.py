import math

print(">>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<")
print(">>>>> Calculo de Segundo Coeficiente Virial B(T) <<<<<")
print(">>>>>>>>>>>>>>>>> Unidades Reducidas <<<<<<<<<<<<<<<<<")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<\n")

# Definimos el Potencial de Stock-Myers como funcion

def stockmyers(sigr,epsr,miur,rr):
    a = sigr/rr
    return 4*epsr*((a**12)-(a**6))-(miur**2)/rr**3

# Definimos la funcion a integrar del segundo coeficiente virial como funcion

def f(U,T,r):
    return (math.exp(-U/T)-1)*r**2

# CASO 2: sigma=sigmaref, epsilon=1.5,2.0,2.5,3.0 , miu=0.0

# Definimos los valores de sigma,epsilon y miu de manera arbitraria

sigmaa = 1.0
epsilona = [1.5,2.0,2.5,3.0]
miua = 0.0

# Definimos los valores de sigma y epsilon de referencia

sigref = 1.0
epsref = 1.0

#epsred = epsilona/epsref
sigred = sigmaa

# Defininimons los valores de la Temperatura reducida
# Tred = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Tred = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Evaluamos la integral numerica del segundo coeficiente virial usando metodo del trapecio
# Definimos los limites de integracion y el intervalo a emplear

liminf = 0.05
limsup = 100
inter = 0.005
n = int((limsup-liminf)/inter)

# Por cada epsilon en la lista epsilona tendremos un archivo con su grafica correspondiente
for k in epsilona:
    # suma = 0.0
    epsred = k/epsref
    archivo = open("eps"+str(int(k*10))+".dat","w")
    archivo.write("@    title \"Segundo Coeficiente Virial B*(T*): Caso 2\" \n")
    archivo.write("@    xaxis  label \"T*\" \n")
    archivo.write("@    yaxis  label \"B*(T*)\" \n")
    # Evaluamos 10 integrales (una por cada Temperatura) por cada eps en la lista epsilona
    for j in Tred:
        # Evaluando la integral numerica
        suma = 0.0
        for i in range(n):
            suma = suma + f(stockmyers(sigred,epsred,miua,liminf+i*inter),j,liminf+i*inter)

        vintegral = (0.5*inter)*(f(stockmyers(sigred,epsred,miua,liminf),j,liminf) + 2*suma + f(stockmyers(sigred,epsred,miua,limsup),j,limsup))

        segcoefvir = -3*vintegral
        archivo.write(str(j) + "        " + str(segcoefvir) + "\n")

    print(" Archivo eps"+str(int(k*10))+".dat generado")
    archivo.close()

print(" \n Ya acabe mi rey :3")
print(" ")








