t = int(input())

for i in range(t):

    n, prev, curr = input().split()
    n = int(n)

    for j in range(2, n + 1):
        temp = curr
        curr += prev
        prev = temp

    print(f"Case #{i + 1}: {curr}")
