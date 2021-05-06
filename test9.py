# Problem 9:
#
# Создайте 3 вложенных друг в друга условия.


old = int(input("Ваш возраст: "))
print("Для входа в ночной клуб:", end="")

if 20 <= old < 22:
    if 22 < 24:
        print("drink")
        if 24 > 25:
            print("pivo")
else:
    print('go')

