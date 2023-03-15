var_input1 = int(input("Введите сумму выручки "))
var_input2 = int(input("Введите сумму издержек "))
# var_input1 = 15
# var_input2 = 20

res = var_input1 - var_input2

if res > 0:
    print(f"Вы в плюсе на {res}")
else:
    print(f"Вы в минусе на {res}")
