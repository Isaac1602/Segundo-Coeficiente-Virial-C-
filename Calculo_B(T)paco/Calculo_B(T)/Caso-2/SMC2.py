def stockmyers(sigr,epsr,miur,rr):
    a = sigr/rr
    return 4*epsr*((a**12)-(a**6))-(miur**2)/rr**3

sigmaa = 1.0
epsilona = [1.5,2.0,2.5,3.0]
miua = 0.0
sigref = 1.0
epsref = 1.0
# epsred = epsilona/epsref
sigred = sigmaa

liminf = 0.95
limsup = 2
inter = 0.005
n = int((limsup-liminf)/inter)

for k in epsilona:
    archivo = open("SMeps"+str(int(k*10))+".dat","w")
    archivo.write("@    title \"Stock-Myers: Caso 2\" \n")
    archivo.write("@    xaxis  label \"r*\" \n")
    archivo.write("@    yaxis  label \"U*(r*)\" \n")
    epsred = k/epsref
    for i in range(n):
        x = liminf+i*inter
        y = stockmyers(sigred,epsred,miua,x)
        archivo.write(str(x) + "	" + str(y) + "\n")

    print(" Archivo SMeps"+str(int(k*10))+".dat Generado")
    archivo.close()

print(" \nYa estufas xD \n")


