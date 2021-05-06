#создайте условие которое определит самое большое и самое маленьеое число из трех

a = 22
b = 98
c = 34

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)

if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)
# if a < b:
#     if b < c:
#         if c > a:
#             print("e")
#         else:
#             print("4")
#     else:
#         print
