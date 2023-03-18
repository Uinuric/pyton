my_list = list(input("Введите элементы списка: ").split())
for el in range(len(my_list)):
    print(f" {el} {my_list[el][0:10]}")
