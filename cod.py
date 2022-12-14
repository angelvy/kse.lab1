import sys

def task_1():
    country = sys.argv[3]
    year = sys.argv[4]

    gold_med = 0
    silver_med = 0
    bronze_med = 0

    with open("athlete_events.tsv", 'r') as file:
        head = file.readlines()
        while line:
            line = file.readlines()
            if not line:
                break






