import sys ,statistics
def get_mean_and_medain():
    if len(sys.argv) >1:
        new_list =[]
        for c in sys.argv[1:] :
            try :
                float(c)
                new_list.append(float(c))
            except ValueError:
                sys.exit("wrong input")    
    else :
        sys.exit("there is no input")

    mean = statistics.mean(new_list)
    medain = statistics.median(new_list)
    if abs(mean - medain)>5:
        return "there is a problem"
    else :

    
        return    f"the mean is :{mean} ,the medain is {medain} "


print(get_mean_and_medain())


