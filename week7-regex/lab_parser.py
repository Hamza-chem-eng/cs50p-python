import re

def parse_lab_data(line):
    d = {}
    k = line.split(",")
    for x in k :
        if match := re.search(r"(\w+): (\d+(?:\.\d+)?)(?: ([A-Za-z/]*))?",x):
            print(match.group(3))
            d[match.group(1)] = (match.group(2),match.group(3))
    return d
if __name__=="__main__":
    print(parse_lab_data(input()))            