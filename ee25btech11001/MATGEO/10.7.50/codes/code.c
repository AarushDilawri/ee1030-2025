#include <math.h>
#include <stdlib.h>

// Computes y values for locus given an array of x values
// A x^2 (y^2 - 1) - B y^2 = 0  => (A x^2 - B) y^2 = A x^2
// => y^2 = (A x^2)/(A x^2 - B)
void compute_locus(double *x_vals, double *y_vals, int n, double A, double B, double C) {
    for (int i = 0; i < n; i++) {
        double x = x_vals[i];
        double denom = A * x * x - B;
        if (denom == 0) {
            y_vals[i] = NAN;  // avoid division by zero
            continue;
        }
        double y2 = (A * x * x) / denom;
        if (y2 < 0) {
            y_vals[i] = NAN;  // no real solution
            continue;
        }
        y_vals[i] = sqrt(y2);  // upper branch
    }
}

