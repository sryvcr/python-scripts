def fib(n: int) -> None:
    """
        print the Fibonacci sequence up to a number n
    """
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a+b
        print()
    return


if __name__ == "__main__":
    n = int(input("please, enter a number: "))
    fib(n)
