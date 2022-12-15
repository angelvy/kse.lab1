import sys

def task_1():
    country_arg = sys.argv[3]  #аргумент країни в параметрі
    year_arg = sys.argv[4]   #аргумент року проведення в параметрі

    gold_med = 0
    silver_med = 0      #поки пусті комірки
    bronze_med = 0

    with open("athlete_events.tsv", 'r') as file:    #відкриваємо наш початковий файл і кажемо що далі від буде називатись 'file'
        head = file.readlines()     #
        while line:                    #запускаємо цикл який буде працювати поки не закінчаться строки
            line = file.readlines()
            if not line:
                break

            line_split = line.split("\t")    #розділяємо строки на частини які видаються потім списком
            name = line_split[1]
            sport = line_split[12]
            medals = line_split[14]
            year = line_split[9]
            team = line_split[7]

            if country_arg == team and year_arg == year:
                if medals == "Gold\n":
                    gold_med += 1
                if medals == "Silver\n":
                    silver_med += 1
                if medals == "Bronze\n":
                    bronze_med += 1
                if gold_med + silver_med + bronze_med <= 10:
                    print(f"{name}, {sport}, {medals}")
                    result = []
                    result.append(f"{name}, {sport}, {medals}")    #додаємо в список результатів

            if medals == "NA\n":
                continue

        if 0 < gold_med + silver_med + bronze_med < 10:
            print("Медалей менше ніж 10")
        if gold_med + silver_med + bronze_med == 0:
            print("У країни відсутні медалі у даний рік")
            exit()
        print(f"{gold_med} золотих медалей, {silver_med} срібних медалей, {bronze_med} бронзових медалей")
        result.append(f"{gold_med} золотих медалей, {silver_med} срібних медалей, {bronze_med} бронзових медалей")














