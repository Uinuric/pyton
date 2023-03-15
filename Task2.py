var_input = int(input("Введите время в секундах "))
#var_input = 5000
var_hour = var_input // 3600
var_min = (var_input - 3600) // 60
var_sec = (var_input - var_hour * 3600 - var_min * 60)

var_hour = var_input // 3600

print(f" {var_hour}:{var_min}:{var_sec}")
