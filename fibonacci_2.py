def fib(n: int) -> None:
    """
        prints the Fibonacci sequence of the first n numbers
    """
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a+b
        print()
    return


if __name__ == "__main__":
    n = int(input("please, enter a number: "))
    fib(n)
