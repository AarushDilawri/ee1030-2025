#include <math.h>

double dot(const double *a, const double *b, int n) {
    double s = 0.0;
    for (int i = 0; i < n; ++i) s += a[i] * b[i];
    return s;
}

/*
 Solve for the parameter t such that the vector P = p0 + t u (position vector from origin)
 makes angle `angle` with u. n is the dimension. ts is an array of length >= 2.
 Returns number of real roots found (0 or 2). If 0, ts[0],ts[1] set to NAN.
*/
int solve(double angle, const double *u, const double *p0, int n, double *ts) {
    double cosA = cos(angle);
    double c2 = cosA * cosA;

    double U = dot(u, u, n);     // u^T u
    double W = dot(u, p0, n);    // u^T p0
    double Q = dot(p0, p0, n);   // p0^T p0

    double one_minus_c2 = 1.0 - c2;
    if (fabs(one_minus_c2) < 1e-15) { // angle ~ 0 or pi => degenerate
        ts[0] = ts[1] = NAN;
        return 0;
    }

    double A = one_minus_c2 * U * U;
    double B = 2.0 * one_minus_c2 * U * W;
    double C = W * W - c2 * U * Q;

    double D = B * B - 4.0 * A * C;
    if (D < 0.0) {
        ts[0] = ts[1] = NAN;
        return 0;
    }

    ts[0] = (-B + sqrt(D)) / (2.0 * A);
    ts[1] = (-B - sqrt(D)) / (2.0 * A);
    return 2;
}

