my_var = int(input("Введите элемент рейтинга: "))
#my_var = 9
my_list = [7, 5, 3, 3, 2]
for el in range(len(my_list)):
    if my_var > my_list[el]:
        my_list.insert(el, my_var)
        break
print(my_list)
