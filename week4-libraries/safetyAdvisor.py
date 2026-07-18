import sys ,random
import cowsay



if len(sys.argv) != 2:
    sys.exit("wrong input")
else :
    chemical = sys.argv[1]
    warnings = [
    f"Warning: {chemical} is hazardous! Wear protective gloves.",
    f"Caution: Always store {chemical} in a cool, dry place.",
    f"Alert: {chemical} requires proper ventilation when handling.",
    f"Safety first: Never mix {chemical} with unknown substances.",
    f"Reminder: Keep {chemical} away from heat and open flames.",
]   
    m = random.choice(warnings)
    cowsay.cow(m)