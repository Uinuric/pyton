var_input = int(input("Введите число "))
# var_input = 3

#num_1 = int(str(var_input) + str(var_input))
#num_2 = int(str(var_input) + str(var_input) + str(var_input))

num_to_str = str(var_input)
num_1 = num_to_str + num_to_str
num_2 = num_to_str + num_to_str + num_to_str
print(f"{var_input + int(num_1) + int(num_2)}")
