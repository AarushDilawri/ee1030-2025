#include <math.h>

void find_points(double u1, double u2, double f, double n1, double n2, double *out) {
    // Compute radius and center
    double r = sqrt(u1*u1 + u2*u2 - f);
    double unorm = sqrt(n1*n1 + n2*n2);

    // Compute contact points
    double px = -u1 + r*(n1/unorm);
    double py = -u2 + r*(n2/unorm);

    double qx = -u1 - r*(n1/unorm);
    double qy = -u2 - r*(n2/unorm);

    out[0] = px;
    out[1] = py;
    out[2] = qx;
    out[3] = qy;
}
