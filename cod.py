import sys


command = sys.argv[2]

if command == "-medals":
    country_arg = sys.argv[3]  #аргумент країни в параметрі
    year_arg = sys.argv[4]   #аргумент року проведення в параметрі
    gold_med = 0
    silver_med = 0      #поки пусті комірки
    bronze_med = 0
    result = []  # пустий список
    amount = 0
    our_years = []    # пусті списки років і країн
    our_countries = []

    with open(sys.argv[1], 'r') as file:    #відкриваємо наш початковий файл і кажемо що далі від буде називатись 'file'
        file.readline()  #прочитали перший рядок, щоб потім його ігнорувати
        line = file.readline()   #починаємо зчитувати наступні рядки
        while line != "":          #запускаємо цикл який буде працювати поки не закінчаться рядки
            line_split = line.split("\t")    #розділяємо строки на частини які видаються потім списком
            name = line_split[1]
            sport = line_split[12]
            medals = line_split[14]
            year = line_split[9]
            team = line_split[6]
            noc = line_split[7]
            our_years.append(year)      #додаємо у створені списки просплітовані роки країни
            our_countries.append(team)
            our_countries.append(noc)
            line = file.readline()
            if country_arg in (team, noc) and year_arg == year and year in line_split:
                if medals != "NA\n":
                    if medals == "Gold\n":
                        gold_med += 1
                    elif medals == "Silver\n":
                        silver_med += 1
                    elif medals == "Bronze\n":
                        bronze_med += 1
                    if amount < 10:
                        print(f"{amount + 1} {name} {sport} {medals}")
                        amount += 1
        else:
            if 0 < gold_med + silver_med + bronze_med < 10:
                print("Медалей менше ніж 10")

            elif gold_med + silver_med + bronze_med == 0:
                print("У країни відсутні медалі у даний рік")

            if year_arg not in our_years:
                print("у цьому році не було олімпіади")
            if country_arg not in our_countries:
                print("ця країна не існує")

            print(f"{gold_med} золотих медалей, {silver_med} срібних медалей, {bronze_med} бронзових медалей")


elif command == "-total":
    year_arg = sys.argv[3]
    result = {}  # словник

    with open(sys.argv[1], 'r') as file:    #відкриваємо наш початковий файл і кажемо що далі від буде називатись 'file'
        file.readline()
        line = file.readline()

        for line in file:
            line_split = line.split("\t")
            medals = line_split[14]
            year = line_split[9]
            team = line_split[6]

            if year_arg == year and medals != "NA\n":
                result.setdefault(team, [0, 0, 0])    # визиваємо зі словника результату країну
                if medals == 'Gold\n':
                    result[team][0] += 1
                elif medals == 'Silver\n':
                    result[team][1] += 1
                elif medals == 'Bronze\n':
                    result[team][2] += 1

        for key, value in result.items():   #key це країна, value це медалі
            value = [str(i) for i in value]    #
            answer = key + ' - ' + ' - '.join(value)
            print(answer)

