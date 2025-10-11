// code.c
#define MAX_N 10

int countCommutingMatrices(int n, int *A, int maxVal) {
    // if any off-diagonal entry of A is non-zero, infinite solutions (a=b)
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (i != j && A[i*n + j] != 0)
                return -1;

    // otherwise finite: count diagonal Bs with a=b
    return maxVal;
}

