import time
import random

def BUUBLESORT(L):
    n = len(L)
    for i in range(0,n):
        for j in range(n-1, i, -1):
            if L[j] < L[j -1]:
                key = L[j]
                L[j] = L[j - 1]
                L[j - 1] = key
    return L

n = 10000
L = list(range(n))
random.shuffle(L)
start = time.time()
BUUBLESORT(L)
final = time.time()
final_time = final - start

print(final_time)
