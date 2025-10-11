#include <stdio.h>
#include <math.h>

void quadratic_roots(double a, double b, double c, double *real1, double *imag1, double *real2, double *imag2) {
    double D = b*b - 4*a*c;
    if (D >= 0) {
        *real1 = (-b + sqrt(D)) / (2*a);
        *imag1 = 0;
        *real2 = (-b - sqrt(D)) / (2*a);
        *imag2 = 0;
    } else {
        *real1 = -b / (2*a);
        *real2 = -b / (2*a);
        *imag1 = sqrt(-D) / (2*a);
        *imag2 = -sqrt(-D) / (2*a);
    }
}

