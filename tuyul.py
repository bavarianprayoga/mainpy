def square(n):
    for i in range(0, n):
        if (i == 0 or i == (n - 1)):
            print("@ " * n)
        else:
            print("@ " + "  " * (n - 2) + "@")

square(9)