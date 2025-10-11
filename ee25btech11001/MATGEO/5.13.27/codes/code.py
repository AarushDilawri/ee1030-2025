def count_commuting(A, n, maxVal):
    for i in range(n):
        for j in range(n):
            if i != j and A[i][j] != 0:
                return -1
    return maxVal

A = [[1, 2],
     [3, 4]]
n = 2
maxVal = 5

res = count_commuting(A, n, maxVal)
print("Number of commuting matrices B = ∞ (infinite)" if res == -1 else f"Number of B = {res}")

