#include <stdio.h>

// Function to compute characteristic polynomial coefficients of a 2x2 matrix
// Input: a11, a12, a21, a22
// Output: coeffs[0] = 1 (λ^2), coeffs[1] = -trace(A), coeffs[2] = det(A)
void char_poly(double a11, double a12, double a21, double a22, double* coeffs) {
    double trace = a11 + a22;
    double det = a11 * a22 - a12 * a21;

    coeffs[0] = 1.0;       // λ^2 coefficient
    coeffs[1] = -trace;    // λ coefficient
    coeffs[2] = det;       // constant term
}

