from functools import lru_cache

@lru_cache(maxsize=None)
def func(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    else:
        return 5*func(n-1) + func(n-2)

A =[]
n = 0

while len(A) < 40:
    val = func(n)
    if val % 2 != 0:
        A.append(val)
        print(val)
    n += 1

print(A[39])
