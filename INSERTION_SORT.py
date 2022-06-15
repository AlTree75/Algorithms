import random
import time


def INSERTION_SORT(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and key < A[i]:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A



n = 50000
A = list(range(n))
random.shuffle(A)
start = time.time()
INSERTION_SORT(A)
final = time.time()
print("starting time: ", start)
print("final time: ", final)
print("total time ", final - start)

