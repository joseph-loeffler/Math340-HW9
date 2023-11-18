import random
import math
import statistics


def E_XgivenYequalsy (y):
    return 1/2*math.sqrt(1-y**2)


def F_EofXgivenY_empirical(list, var):
    return len([E for E in list if E<=var])/len(list)


if __name__ == "__main__" : 

    trials = 10000
    uber_list = []
    list_of_Ys = []

    for _ in range(trials):
        num_of_points = 1000

        points = []
        y = random.uniform(-1, 1)
        list_of_Ys.append(y)

        while len(points) < num_of_points :
            x = random.uniform(-1, 1)
            # y = random.uniform(-1, 1)

            if (x > 0) and (x**2 + y**2 < 1) :
                d = {
                    "x": x, 
                    "y": y
                }
                points.append(d)

        uber_list.append(statistics.mean(point['x'] for point in points))

    fname = "file_output.txt"
    file = open(fname, "w")
    file.write("k\tF_E(X|Y)_(k)\tPr(0.5*sqrt(1-Y^2) <= k)\n")

    for i in range(101):
        k = i/100
        ret = F_EofXgivenY_empirical(uber_list, k)
        PrFuncSmlrThank = len([y for y in list_of_Ys if (0.5*math.sqrt(1-y**2))<=k])/len(list_of_Ys)
        file.write(f"{k}\t{ret}\t{PrFuncSmlrThank}\n")

    file.close()
    
    # fname = "file_output.txt"

    # file = open(fname, "w")

    # file.write("y values:\tE(X|Y)\n")
    # for elem in uber_list:
    #     file.write(str(elem[0]) + "\t" + str(elem[1]) + "\n")

    # file.close()