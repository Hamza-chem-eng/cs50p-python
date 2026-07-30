import csv , random
with open("data.csv","w") as file:
    fieldnames = ["temp","pressure","flow rate"]
    writer = csv.DictWriter(file,fieldnames = fieldnames)
    writer.writeheader()
    for _ in range(1,11):
        writer.writerow({"temp":random.randint(0,999),
        "pressure":random.randint(0,50),
        "flow rate":random.randint(0,100)})