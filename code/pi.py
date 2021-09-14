import math


def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result


def estimate_pi():
    epsilon = 10**-15
    sigma = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4*k) * (1103 + 26390*k)
        den = factorial(k)**4 * 396**(4*k)
        last = factor * num / den
        sigma = sigma + last

        if abs(last) < epsilon:
            break

        k = k + 1
    return 1 / sigma


print(estimate_pi())
print(math.pi)
print(abs(estimate_pi() - math.pi))
