import random
import math
import statistics


def E_XgivenYequalsy (y):
    return 1/2*math.sqrt(1-y**2)


def F_EofXgivenY_empirical(list, var):
    return len([E for E in list if E<=var])/len(list)

def F_EofXgivenY_theoretical(k):
    return ((2*math.asin(2*k)-4*k*math.sqrt(1-4*k**2))/math.pi) - ((2*math.asin(2*0)-4*0*math.sqrt(1-4*0**2))/math.pi)


if __name__ == "__main__" : 

    trials = 1000
    Expectation_list = []
    list_of_Ys = []

    for _ in range(trials):
        num_of_points = 100

        points = []
        y = random.uniform(-1, 1)
        list_of_Ys.append(y)

        while len(points) < num_of_points :
            x = random.uniform(-1, 1)
            # y = random.uniform(-1, 1)

            if (x > 0) and (x**2 + y**2 <= 1) :
                d = {
                    "x": x, 
                    "y": y
                }
                points.append(d)
        ExpectationOfXgivenY = statistics.mean([point['x'] for point in points])
        if ExpectationOfXgivenY > 0.5:
            print([point["y"] for point in points])
        Expectation_list.append(ExpectationOfXgivenY)

    fname = "file_output.txt"
    file = open(fname, "w")
    file.write("k\ttheoretical\tempirical\n")

    for i in range(101):
        k = i/100
        empirical = F_EofXgivenY_empirical(Expectation_list, k)
        if k <= 0.5:
            theoretical = F_EofXgivenY_theoretical(k)
        else:
            theoretical = 1

        file.write(f"{k}\t{theoretical}\t{empirical}\n")


        # PrFuncSmlrThan_k = len([y for y in list_of_Ys if (0.5*math.sqrt(1-y**2))<=k])/len(list_of_Ys)
        # file.write(f"{k}\t{ret}\t{PrFuncSmlrThan_k}\n")

        

    file.close()
    
    # fname = "file_output.txt"

    # file = open(fname, "w")

    # file.write("y values:\tE(X|Y)\n")
    # for elem in uber_list:
    #     file.write(str(elem[0]) + "\t" + str(elem[1]) + "\n")

    # file.close()