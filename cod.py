import sys



country_arg = sys.argv[3]  #аргумент країни в параметрі
year_arg = sys.argv[4]   #аргумент року проведення в параметрі

gold_med = 0
silver_med = 0      #поки пусті комірки
bronze_med = 0
result = []
with open(sys.argv[1], 'r') as file:    #відкриваємо наш початковий файл і кажемо що далі від буде називатись 'file'
    file.readline()  #!!!!!!!!!!
    line = file.readline()
    while line != "":                  #запускаємо цикл який буде працювати поки не закінчаться строки
        # line = file.readline()
        # if not line:
        #     continue

        line_split = line.split("\t")    #розділяємо строки на частини які видаються потім списком
        name = line_split[1]
        sport = line_split[12]
        medals = line_split[14]
        year = line_split[9]
        team = line_split[6]
        noc = line_split[7]
        line = file.readline()
        if country_arg in (team, noc) and year_arg == year and year in line_split:
            #if year in line_split and year == year_arg:
                if medals != "NA\n":
                    if medals == "Gold\n":
                        gold_med += 1
                    elif medals == "Silver\n":
                        silver_med += 1
                    elif medals == "Bronze\n":
                        bronze_med += 1
                    #print(f"{noc}")
    else:
        #print(f"{name}, {sport}, {medals}")
        #print(gold_med)
        #if gold_med + silver_med + bronze_med >= 10:
            #print(f"{name}, {sport}, {medals}")

        result.append(f"{name}, {sport}, {medals}")    #додаємо в список результатів
        #print(f"{name}, {sport}, {medals}")
        print(result)


    if 0 < gold_med + silver_med + bronze_med < 10:
        print("Медалей менше ніж 10")

    if gold_med + silver_med + bronze_med == 0:
        print("У країни відсутні медалі у даний рік")



    print(f"{gold_med} золотих медалей, {silver_med} срібних медалей, {bronze_med} бронзових медалей")
    result.append(f"{gold_med} золотих медалей, {silver_med} срібних медалей, {bronze_med} бронзових медалей")

