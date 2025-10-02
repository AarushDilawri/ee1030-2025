// code.c
#include <stdio.h>

// Function to solve system of 2 equations in 2 unknowns
// Equations: a1*x + b1*y + c1 = 0
//            a2*x + b2*y + c2 = 0
// Returns:
//   1 = unique solution
//   2 = infinite solutions
//   0 = no solution
int solve_linear(double a1, double b1, double c1,
                 double a2, double b2, double c2,
                 double *x, double *y) {
    double det = a1*b2 - a2*b1;
    if(det != 0) {
        *x = (b1*c2 - b2*c1) / det;
        *y = (c1*a2 - c2*a1) / det;
        return 1; // unique solution
    }
    // det = 0, check proportionality
    if(a1*b2 == a2*b1 && a1*c2 == a2*c1 && b1*c2 == b2*c1) {
        return 2; // infinite solutions
    }
    return 0; // no solution
}

