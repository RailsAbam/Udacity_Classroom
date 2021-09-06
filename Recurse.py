


def count(n):
    if n <= 0:
        print(n + 1 )
    else:
        print("Blast off")
print(count(3))


def fib(n: int):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)
print(fib(5))
print(fib(10))


