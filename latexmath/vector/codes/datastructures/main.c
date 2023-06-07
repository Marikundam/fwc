#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include "lib.h"
int main()
{

	Node *a, *b, *c, *d, *e1, *m_1, *m_2, *n_1,*n_2, *m_1_, *n_1_, *dp_m,  *dp_n;
	
	double l= 5;
	double m= 9;
	double theta = M_PI * 1/6;


	double m1,m2,n1,n2,p,q;
	double angABD,angCBA;
	int *x,*y;

	a=loadtxt("a.dat");
	e1=loadtxt("e1.dat");


	b =createMatrix(2,1);
	b =mat_val(e1,m);



	double cosine = cos(theta);
	double sine = sin(theta);

	d=createMatrix(2,1);
	x=(int *)malloc(2*sizeof(int));
	x[0] = cosine;
	x[1] = -sine;
	d = assign(2,1,x);
	d = mat_val(d,l);
	

	c =createMatrix(2,1);
	y=(int *)malloc(2*sizeof(int));
	y[0] = cosine;
	y[1] = sine;
	c = assign(2,1,y);
	c =mat_val(c,l);
	

	m_1 =linalg_sub(b,c);
	m_2 =linalg_sub(b,a);
	n_1 =linalg_sub(d,b);
	n_2 =linalg_sub(a,b);

	m1 = linalg_norm(m_1,2,1);
	m2 = linalg_norm(m_2,2,1);
	n1 = linalg_norm(n_1,2,1);
	n2 = linalg_norm(n_2,2,1);

	m_1_ = transpose(m_1);
	n_1_ = transpose(n_1);

	dp_m = matmul(m_1_,m_2,1,1);
	p = get(dp_m,0,0);
	angCBA =acos(p / (m1*m2))*(180/M_PI);

	dp_n = matmul(n_1_,n_2,1,1);
	q = get(dp_n,0,0);
	angABD =acos(q / (n1*n2))*(180/M_PI);

	
	if(round(angABD)==round(angCBA))
	{
		printf("âˆ ABD = âˆ CBA\n");
	}
	

	
	save("b.dat",b,2,1);
	save("c.dat",c,2,1);
	save("d.dat",d,2,1);
	return 0;
}

