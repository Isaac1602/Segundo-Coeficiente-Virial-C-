#include <stdio.h>
#include <math.h>
#include <stdlib.h>

long double  stockmayer (long double dominio, long double mu){
    long double r, potencial;
    r = dominio;
    potencial = 4*(pow(1/r, 12)- pow(1/r,6))-pow(mu, 2)/pow(r, 3);
    return potencial;
}

void integral_trapecio (long double limite_inferior, long double limite_superior, 
                         long double *rango,  long double intervalo, int nsteps, long double  T, long double mu,
                         long double *integral ){

    //FILE *file;
    
    long double  *stockmayer_array = (long double  *)malloc(nsteps *sizeof(float));
    long double  suma, evalucacion_SM, evalucacion_SMf , valor_integral;
    int i;
    //char filename[256];

    //snprintf(filename, sizeof(filename), "segunodcoef_sig_10eps%.2LeT%Le.dat", mu, T);
    //file = fopen(filename, "w");
    //fprintf(file, "Los datos del sgundo virial con sigma = 0.0 y mu = %Le con T = %Le son \n", mu, T );

    suma = rango[0]*rango[0]*(exp(-stockmayer(rango[0], mu)/T)-1);
    //fprintf(file, "%Le %Le\n", rango[0], suma);

    for (i = 1; i <= nsteps-2;i++){
        evalucacion_SM = rango[i]*rango[i]*(exp(-stockmayer(rango[i], mu)/T)-1);
        //fprintf(file, "%Le %Le\n", rango[i], evalucacion_SM);
        suma = suma + 2*evalucacion_SM;
    }
    evalucacion_SMf = rango[nsteps-1]*rango[nsteps-1]*(exp(-stockmayer(rango[nsteps-1], mu)/T)-1);
    suma = suma + evalucacion_SMf;
    //fprintf(file, "%Le %Le\n", rango[nsteps-1], evalucacion_SM);

    valor_integral = -(intervalo)*0.5*suma;
    *integral = valor_integral;
    //fprintf(file, "Integral = %Le", valor_integral);
}


int main (){
    
    FILE *archivo_temperatura;
    char nombrearchivo[200];

    int nsteps = 100000, i, j, k;
    long double  *rango = (long double  *)malloc(nsteps * sizeof(long double));
   
    long double  temperaturas [10] = {1.0, 2. , 3. , 4. ,5. ,6. ,7. , 8. ,9. , 10.};
    long double  limite_inferior = 0.5, limite_superior = 100.5, posicion, intervalo;
    long double  mus[5] = {0.2, 0.4, 0.6, 0.8, 1.0};
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
    for (j = 0; j<= 4; j++)
    {
        snprintf(nombrearchivo, sizeof(nombrearchivo), "SegCoefVirSigma1.0Eps1.0Mu%.2Le.dat", mus[j]);
        archivo_temperatura = fopen(nombrearchivo, "w");
        printf ("entra\n ");
        for (k = 0; k<=9; k++){
            integral_trapecio(limite_inferior, limite_superior, rango, 
                            intervalo, nsteps, temperaturas[k], mus[j], &integral);
            
            fprintf(archivo_temperatura,"%14.8Le %14.8Le\n", temperaturas[k], integral);
            
            printf("%Le %Le \n", temperaturas[k], mus[j]);
            }
       fclose(archivo_temperatura);    
            
    }
    return 0;
    
}