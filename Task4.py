var_input = int(input("Введите число "))
# var_input = 365548

var_max = var_input % 10
var_input = var_input // 10

while var_input > 0:
    if var_input % 10 > var_max:
        var_max = var_input % 10
    var_input = var_input // 10
print(f"{var_max}")
