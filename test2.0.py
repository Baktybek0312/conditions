a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    print(a, "Наибольшее число")
    if b > c:
        print("Ниболше число: с =", c)
    elif b < c:
        print()
    else:
        print("")
