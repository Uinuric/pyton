var_input1 = int(input("Введите результат первого дня "))
var_input2 = int(input("Введите желаемый результат "))
# var_input1 = 2
# var_input2 = 4

res = var_input1
day = 2
res = res + res * 0.1
while res < var_input2:
    day += 1
    res = res + res * 0.1
#   print(f" {res}")
print(f"Спортсмен достигнет желаемого результата на {day} день")
