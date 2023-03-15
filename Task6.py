var_input1 = int(input("Введите сумму выручки "))
var_input2 = int(input("Введите сумму издержек "))
# var_input1 = 40
# var_input2 = 20

res = var_input1 - var_input2

if res > 0:
    print(f"Вы в плюсе на {res}")
    print(f"Ваша рентабельность составила  {var_input1 // var_input2}")
    # var_input3 = 5
    var_input3 = int(input("Введите количество сотрудников "))
    print(f"Ваша прибыль в расчете на 1 сотрудника  {res / var_input3}")
else:
    print(f"Вы в минусе на {res}")
