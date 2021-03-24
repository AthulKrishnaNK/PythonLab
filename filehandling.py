import csv
fname=["depname","teacher","experience"]
with open("departments.csv","w") as csvfile:
    writer = csv.DictWriter(csvfile)
    writer.writeheader()
    writer.writerow(["english","amrutha",5])
with open('departments.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile,usecols = fname)
    for column in reader:
        print(reader["depname"])
