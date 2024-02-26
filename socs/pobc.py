t = int(input())
total = []

for i in range(t):
    txt = list(map(int, input().split()))
    # txt2 = txt[-1]

    print(txt)
    # print(txt2)

    num1 = txt[0]
    num2 = txt[-1]

    print(num1)
    print(num2)

    total.append(num1 + num2)

for i, val in enumerate(total):
    print(f"Case #{i + 1}: {val}")
