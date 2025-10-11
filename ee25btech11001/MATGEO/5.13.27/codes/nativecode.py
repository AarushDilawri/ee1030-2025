import ctypes

lib = ctypes.CDLL("./code.so")
lib.countCommutingMatrices.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int]
lib.countCommutingMatrices.restype = ctypes.c_int

n = 2
A = [1, 2, 3, 4]
maxVal = 5
A_c = (ctypes.c_int * (n*n))(*A)

res = lib.countCommutingMatrices(n, A_c, maxVal)
print("Number of commuting matrices B = ∞ (infinite)" if res == -1 else f"Number of B = {res}")

