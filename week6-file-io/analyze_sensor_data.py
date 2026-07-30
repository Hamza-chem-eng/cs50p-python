import csv, os 
max_temp = 0 
temp = []
with open("data.csv") as file :
    reader = csv.DictReader(file)
    for row in reader :
        temp.append(float(row["temp"]))
        
        if float(row["temp"]) > max_temp:
            max_temp  = float(row["temp"])
            max_pressure = row["pressure"]
            max_flow_rate = row["flow rate"]
average = sum(temp)/ len(temp)
with open("report.csv","w") as file:
    write = csv.writer(file)
    write.writerow(["Metric","Value"])
    write.writerow(["average temp",average])
    write.writerow(["max temp",max(temp)])
    write.writerow(["min temp",min(temp)])
