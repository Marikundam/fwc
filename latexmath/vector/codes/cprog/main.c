#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include"lib.h"    

int main()
{
    double c = 5;
    double b = 9;
    double theta = M_PI * 1 / 6;

    double **A, **B, **D, **C, **e1;
    double **m_1, **m_2, **n_1, **n_2;
    double m1, m2, n1, n2;
    double dot_product_m, dot_product_n;
    double angABD, angCBA;

    A = loadtxt("a.dat",2, 1);
    e1 = loadtxt("e1.dat",2, 1);
   
    B = createMat(2,1);
    B = mult_int(b, e1, 2, 1);
    
    double cosine = cos(theta);
    double sine = sin(theta);
    
    D = createMat(2,1);
    D[0][0]=cosine;
    D[1][0]=-sine;

    D = mult_int(c, D, 2, 1);

    C = createMat(2,1);
    C[0][0]=cosine;
    C[1][0]=sine;

    C = mult_int(c, C, 2, 1);
    
    m_1 = linalg_sub(B, C, 2, 1);
    m_2 = linalg_sub(B, A, 2, 1);
    n_1 = linalg_sub(D, B, 2, 1);
    n_2 = linalg_sub(A, B, 2, 1);

    m1 = linalg_norm(m_1, 2);
    m2 = linalg_norm(m_2, 2);
    n1 = linalg_norm(n_1, 2);
    n2 = linalg_norm(n_2, 2);

    dot_product_m = matmul(transpose(m_1,2,1),m_2,1,2,1);
	angCBA = acos(dot_product_m / (m1*m2))*(180/M_PI);
	dot_product_n = matmul(transpose(n_1,2,1),n_2,1,2,1);
	angABD = acos(dot_product_n / (n1*n2))*(180/M_PI);

    if(round(angABD) == round(angCBA))
    {
        printf("âˆ  ABD = âˆ  CBA\n");
    }
    save_B(B,2,1);
    save_C(C,2,1);
    save_D(D,2,1);
    return 0;
}
