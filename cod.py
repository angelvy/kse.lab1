import sys

def task_1():
    country_arg = sys.argv[3]
    year_arg = sys.argv[4]

    gold_med = 0
    silver_med = 0
    bronze_med = 0

    with open("athlete_events.tsv", 'r') as file:
        head = file.readlines()
        while line:
            line = file.readlines()
            if not line:
                break

            line_split = line.split("\t")
            name = line_split[1]
            sport = line_split[12]
            medals = line_split[14]
            year = line_split[9]
            team = line_split[6]










