def stockmyers(sigr,epsr,miur,rr):
    a = sigr/rr
    return 4*epsr*((a**12)-(a**6))-(miur**2)/rr**3

sigmaa = [1.5,2.0,2.5,3.0]
epsilona = 1.0
miua = 0.0
sigref = 1.0
epsref = 1.0
epsred = epsilona/epsref

liminf = 1.0
limsup = 10.0
inter = 0.005
n = int((limsup-liminf)/inter)

for k in sigmaa:
    archivo = open("SMsig"+str(int(k*10))+".dat","w")
    archivo.write("@    title \"Stock-Myers: Caso 3\" \n")
    archivo.write("@    xaxis  label \"r*\" \n")
    archivo.write("@    yaxis  label \"U*(r*)\" \n")
    sigred = k/sigref
    for i in range(n):
        x = liminf+i*inter
        y = stockmyers(sigred,epsred,miua,x)
        archivo.write(str(x) + "	" + str(y) + "\n")

    print(" Archivo SMsig"+str(int(k*10))+".dat Generado")
    archivo.close()

print(" \nYa estufas xD \n")


