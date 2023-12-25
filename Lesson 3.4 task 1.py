import csv

with open("Crimes.csv") as file_to_read:
    reader = csv.reader(file_to_read)
    crime_list = {}
    for line in reader:
        if line[5] not in crime_list:
            crime_list[line[5]] = 1
        else:
            crime_list[line[5]] += 1
    max_crimes = max(crime_list, key=crime_list.get)
    print(max_crimes)
