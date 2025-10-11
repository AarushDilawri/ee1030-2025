#include <stdio.h>
#include <math.h>

/*
  particle_endpoints:
    n         : number of circles (compute P1..Pn)
    px, py    : output arrays of length n (filled with P_k coordinates)
    theta_out : output array of length n (filled with theta_k, the angle after finishing C_k)
*/
void particle_endpoints(int n, double *px, double *py, double *theta_out) {
    double theta = 0.0;
    for (int k = 1; k <= n; ++k) {
        double r = (double)k;
        /* arc length on C_k = k, radius = k => delta_theta = k/k = 1.0 rad */
        double delta = 1.0;
        theta += delta;
        px[k-1] = r * cos(theta);
        py[k-1] = r * sin(theta);
        if (theta_out != NULL) theta_out[k-1] = theta;
    }
}

