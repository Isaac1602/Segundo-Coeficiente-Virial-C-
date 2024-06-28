#include <stdio.h>
#include <math.h>
#include <stdlib.h>

long double  stockmayer (long double dominio, long double epsilon, long double sigma){
    long double r, potencial;
    r = dominio;
    potencial = 4*epsilon*(pow(sigma/r, 12)- pow(sigma/r,6));
    return potencial;
}

void integral_trapecio (long double limite_inferior, long double limite_superior, 
                         long double *rango,  long double intervalo, int nsteps, long double  T, long double concentracion,
                         long double *integral ){

    //FILE *file;
    
    long double  *stockmayer_array = (long double  *)malloc(nsteps *sizeof(float));
    long double  suma1, suma2, suma3, evalucacion_SM, evalucacion_SMf , valor_integral;
    int i;
    char filename[256];

// para B11
    suma1 = rango[0]*rango[0]*(exp(-stockmayer(rango[0], 1.0, 1.0)/T)-1);

    for (i = 1; i <= nsteps-2;i++){
        evalucacion_SM = rango[i]*rango[i]*(exp(-stockmayer(rango[i], 1.0, 1.0)/T)-1);
        suma1 = suma1 + 2*evalucacion_SM;
    }
    evalucacion_SMf = rango[nsteps-1]*rango[nsteps-1]*(exp(-stockmayer(rango[nsteps-1], 1.0, 1.0)/T)-1);
    suma1 = suma1 + evalucacion_SMf;

// para B12

    suma2 = rango[0]*rango[0]*(exp(-stockmayer(rango[0], sqrt(1.5), sqrt(1.5))/T)-1);
    for (i = 1; i <= nsteps-2;i++){
        evalucacion_SM = rango[i]*rango[i]*(exp(-stockmayer(rango[i], sqrt(1.5), sqrt(1.5))/T)-1);
        suma2 = suma2+ 2*evalucacion_SM;
    }
    evalucacion_SMf = rango[nsteps-1]*rango[nsteps-1]*(exp(-stockmayer(rango[nsteps-1], sqrt(1.5), sqrt(1.5))/T)-1);
    suma2 = suma2 + evalucacion_SMf;

// para B22
    suma3 =  rango[0]*rango[0]*(exp(-stockmayer(rango[0], 1.5, 1.5)/T)-1);
    for (i = 1; i <= nsteps-2;i++){
        evalucacion_SM = rango[i]*rango[i]*(exp(-stockmayer(rango[i], 1.5, 1.5)/T)-1);
        suma3 = suma3 + 2*evalucacion_SM;
    }
    evalucacion_SMf = rango[nsteps-1]*rango[nsteps-1]*(exp(-stockmayer(rango[nsteps-1], 1.5, 1.5)/T)-1);
    suma3 = suma3 + evalucacion_SM;


    valor_integral = -(intervalo)*0.5*(concentracion*concentracion*suma1 
                      +2*concentracion*(1-concentracion)*suma2 +(1.0-concentracion)* (1.0-concentracion)*suma3) ;
    *integral = valor_integral;
}


int main (){
    
    FILE *archivo_temperatura;
    char nombrearchivo[200];

    int nsteps = 100000, i, j, k;
    long double  *rango = (long double  *)malloc(nsteps * sizeof(long double));
   
    long double  temperaturas [10] = {1.0, 2. , 3. , 4. ,5. ,6. ,7. , 8. ,9. , 10.};
    long double  limite_inferior = 0.5, limite_superior = 100.5, posicion, intervalo;
    long double  concentraciones[3] = {0.3, 0.5, 0.7};
    long double  integral;
    
    intervalo = (limite_superior-limite_inferior)/nsteps;
    posicion = limite_inferior;

    for (i = 0; i<nsteps; i++){
                rango[i] = posicion;
                posicion = posicion + intervalo;
    }
    printf("%Le\n", posicion);
    printf("%Le \n", rango[1000]);
    
    integral = 0.;
    for (j = 0; j<= 2; j++)
    {
        snprintf(nombrearchivo, sizeof(nombrearchivo), "SegCoefVirSig10Eps10Con%.2Le.dat", concentraciones[j]);
        archivo_temperatura = fopen(nombrearchivo, "w");
        printf ("entra\n ");
        for (k = 0; k<=9; k++){
            integral_trapecio(limite_inferior, limite_superior, rango, 
                            intervalo, nsteps, temperaturas[k], concentraciones[j], &integral);
            
            fprintf(archivo_temperatura,"%14.8Le %14.8Le\n", temperaturas[k], integral);
            
            printf("%Le %Le \n", temperaturas[k], concentraciones[j]);
            }
       fclose(archivo_temperatura);    
            
    }
    return 0;
    
}
