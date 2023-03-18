my_list = input("Введите элементы списка: ")
# print(my_list)
count_el = int(len(my_list) / 2)
end_el = int(len(my_list))
end_list = []
for el in range(count_el):
    end_list.append(my_list[2 * el + 1])
    end_list.append(my_list[2 * el])
if len(my_list) % 2 > 0:
    end_list.append(my_list[end_el - 1])
#     el = el + 1
print(end_list)
