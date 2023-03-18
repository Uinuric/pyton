my_var = int(input("Введите месяц: "))
# my_var = 6
winter_list = [12, 1, 2]
spring_list = [3, 4, 5]
summer_list = [6, 7, 8]
autumn_list = [9, 10, 11]
season = {'зима': winter_list, 'весна': spring_list, 'лето': summer_list, 'осень': autumn_list}
# season = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето':[6, 7, 8], 'осень':[9, 10, 11]}
if my_var in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    for el in season:
        if my_var in season[el]:
            #        print(el, season[el])
            print(f"Ваш выбор :  {el}")
else:
    print(f"Вы ввели число не принадлежащее к месяцам")
