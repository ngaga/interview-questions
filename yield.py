# TODO: read this https://google.github.io/styleguide/pyguide.html
# TODO: try pylint
# TODO: test this https://wiki.python.org/moin/Generators

import numpy

def isPrime(n):
    if n % 2 == 0:
        return False
    else:
        borne = int(numpy.sqrt(n)) + 1
        for i in range(3, borne, 2):
            if n % i == 0:
                return False
    return True

def nombres_premiers(borne_max = None):
    yield 2
    i = 3
    while not borne_max or i <= borne_max:
        if isPrime(i):
            yield i
        i = i + 2

def primeGreaterThan(n):
    for i in nombres_premiers():
        if i >= n:
            return i

print(primeGreaterThan(101548))
