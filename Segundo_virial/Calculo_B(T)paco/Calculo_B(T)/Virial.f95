program Virial_B
    implicit double precision(a-h,o-z)
    
    integer(4) :: T
    real(8) :: r, mu, sigma, epsilon, h
    real(8), dimension (:), allocatable :: U
    
    write(6,*)'	'
    write(6,*)'****************************************************************************'
    write(6,*)'			Cálculo del Segundo coeficiente virial'
    write(6,*)'				(Unidades reducidas)'
    write(6,*)'****************************************************************************'
    write(6,*)'	'

    write(6,*)'Por favor ingrese los parametros moleculares para epsilon y sigma:'
    write(6,*)'	'
    write(6,*)'Epsilon: '
    read(5,*)epsilon
    write(6,*)'Sigma: '
    read(5,*)sigma
    write(6,*)'Mu: '
    read(5,*)mu
    write(6,*)'	'
    write(6,*)'Para que temperatura desea calcular el segundo coeficiente virial:'
    read(5,*)h

    call Integral(epsilon,sigma,mu,h)

contains
    subroutine Integral(epsilon,sigma,mu,h)
        implicit double precision (a-h,o-z)
        real(8), intent(in) :: epsilon, sigma, mu
        real(8) :: r, a, b, suma, vintegral
!        real(8), dimension(:,:), allocatable :: suma, vintegral
        integer(4) :: n, l
        
        write(6,*)'Inserte los límites de integración:'
        write(6,*)'Límite inferior'
        read(5,*)a
        write(6,*)'Límite superior'
        read(5,*)b
        write(6,*)'Numero de particiones: '
        read(5,*)n
        h = (b-a)/float(n)	
        write(6,*)'     '

        suma = 0.0
        write(6,*)a

        do l = 1, n-1
            suma = suma + 2*Mayer(a+l*h,epsilon,sigma,mu,h)
        enddo
	
        vintegral = (0.5*h)*(Mayer(a,epsilon,sigma,mu,h) + suma + Mayer(b,epsilonr,sigmar,mu,h))
        write(6,*)' La aproximación de la integral es: ',vintegral
        write(6,*)'     '
    end subroutine Integral

    function Mayer(r,epsilon,sigma,mu,h)
        implicit double precision(a-h,o-z)
        real(8), intent(in) :: r, epsilon, sigma, mu 
        real(8), parameter :: K = 1.380649E-23, epsref = 118.63, sigmaref = 3.499
        real(8) :: mu1, epsilonr, sigmar, dm
        integer :: i, j, g
        real(8), dimension (:), allocatable :: U, T
        real(8), dimension (:,:), allocatable :: May

        allocate(U(0:6))
        allocate(T(0:9))
        allocate(May(0:9,0:6))

!        g = int(mu/0.2) 

        epsilonr = epsilon/epsref
        sigmar = sigma/sigmaref        

        mu1 = 0.0
        U = 0.0
        T = 0.0
        May = 0.0
        g = 0

        do j = 0, 9
            T(j) = k*(j+1)/epsref
        end do
         
        do i = 0, 6
            U(i) = 4*epsilonr*((sigmar/r)**12 - (sigmar/r)**6) - (mu1**2)/(r**3)        
            do j = 0, 9
                May(j,i) = (EXP(-(U(i)/T(j)))-1)*(r**2)
            end do
            do while(g /= 0)
                dm = mu - mu1
                g = g + 1
            end do
            mu1 = mu1 + 0.2
        end do  

        Mayer = May(g,h-1)

    end function Mayer 
   
end program 
