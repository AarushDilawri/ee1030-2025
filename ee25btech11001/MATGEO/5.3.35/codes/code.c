#include <stdio.h>

// Function to find r such that the lines are coincident
// Lines: a1*x + b1*y + c1 = 0
//        a2*x + (-r)*y + c2 = 0
double find_r(double a1, double b1, double c1, double a2, double c2) {
    // Since line2 normal = (a2, -r), it must be proportional to (a1, b1)
    // So, a2/a1 = (-r)/b1  AND  c2/c1 = a2/a1
    double k = a2 / a1; 
    double r = -k * b1; 
    return r;
}

