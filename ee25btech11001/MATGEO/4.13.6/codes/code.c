#include <stdio.h>
#include <math.h>

// Function to compute inner product of two vectors
double inner_product(int n, double *u, double *v) {
    double sum = 0.0;
    for(int i=0; i<n; i++) {
        sum += u[i]*v[i];
    }
    return sum;
}

// Function to compute locus equation value at point P
// Equation: P^T (u u^T - D^2 I) P + (-(D^2+alpha)u + 2D^2 A)^T P + ((D^2+alpha)^2)/4 - D^2 A^T A
// Returns double value (should be 0 on the locus)
double locus_value(int n, double *A, double *B, double *P, double D) {
    // Compute u = A - B
    double u[10];  // assume dimension <= 10 for simplicity
    for(int i=0; i<n; i++) {
        u[i] = A[i] - B[i];
    }

    // Compute alpha = A^T A - B^T B
    double alpha = inner_product(n, A, A) - inner_product(n, B, B);

    // Compute P^T (u u^T - D^2 I) P
    double uuT_P[n];
    for(int i=0; i<n; i++) {
        uuT_P[i] = u[i]*inner_product(n, u, P);
    }
    double quad = inner_product(n, P, uuT_P);

    // Subtract D^2 * (P^T P)
    quad -= D*D * inner_product(n, P, P);

    // Compute linear term: (-(D^2+alpha)u + 2D^2 A)^T P
    double coeff[n];
    for(int i=0; i<n; i++) {
        coeff[i] = -(D*D+alpha)*u[i] + 2*D*D*A[i];
    }
    double lin = inner_product(n, coeff, P);

    // Constant term
    double constant = ((D*D+alpha)*(D*D+alpha))/4.0 - D*D*inner_product(n, A, A);

    return quad + lin + constant;
}
