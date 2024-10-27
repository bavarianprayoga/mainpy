def result():
    N = input().strip()
    n = len(N)

    if n < 3:
        return "Kamu"

t = int(input())

for _ in range(t):
    result = solve()
    print(result)