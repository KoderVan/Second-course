from itertools import takewhile
import itertools


def isprime(n):
    d = 2
    while n % d != 0 and n >= d:
        d += 1
    return d == n


def primes():
    i = 2
    while True:
        if isprime(i):
            yield i
        i += 1


def main():
    print(list(itertools.takewhile(lambda x: x <= 31, primes())))


if __name__ == '__main__':
     main()
