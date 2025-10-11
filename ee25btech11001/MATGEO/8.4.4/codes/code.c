#include <math.h>

// Function to compute ellipse coefficients A, B, C
// Equation: A*x^2 + B*y^2 = C
// Returns 0 on success
int ellipse_equation(double *A, double *B, double *C,
                     double x0, double y0, double e)
{
    double V11 = 1.0 - e*e;
    double V22 = 1.0;

    double val = V11*x0*x0 + V22*y0*y0;
    double scale = 1.0 / val;

    *A = V11 * scale;
    *B = V22 * scale;
    *C = 1.0;

    return 0;
}
