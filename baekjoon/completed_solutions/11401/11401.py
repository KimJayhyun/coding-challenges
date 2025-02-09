def power(x, y, n):
    if x == 1:
        return 1

    if y == 1:
        return x % n

    half = power(x, y // 2, n)

    if y % 2 == 0:
        return (half * half) % n
    else:
        return (half * half * x) % n


def factorial(x, n):
    fact = 1

    for i in range(2, x + 1):
        fact = (fact * i) % n

    return fact


def solution(n, k, DIVISOR):

    return (
        factorial(n, DIVISOR)
        * power(factorial(k, DIVISOR) * factorial(n - k, DIVISOR), DIVISOR - 2, DIVISOR)
    ) % DIVISOR


def main():
    import sys

    n, k = map(int, sys.stdin.readline().split(" "))

    DIVISOR = 1000000007

    print(solution(n, k, DIVISOR))


if __name__ == "__main__":
    main()
