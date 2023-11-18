import statistics
import numpy as np


def jointPDF_theoretical(x, y, z):
    if 0<=z and z<=y and y<=x and x<=1:
        return 1/(x*y)
    else:
        return 0



if __name__ == "__main__" : 

    trials = 2**16
    vectors = []

    for _ in range(trials):
        L1 = np.random.uniform(0,1)
        L2 = np.random.uniform(0,L1)
        L3 = np.random.uniform(0,L2)

        vectors.append((L1, L2, L3))

    for _ in range(100):
        x = np.random.uniform(0,1)
        y = np.random.uniform(0,x)
        z = np.random.uniform(0,y)
        tup = (x, y, z)
        print(f"tup: {tup}")
        list_smaller_than = []
        for v in vectors:
            if v[0] <= x and v[1] <= y and v[2] <= z:
                list_smaller_than.append(v)
        
        empiricalJointPDF = len(list_smaller_than)/trials
        theoreticalJointPDF = jointPDF_theoretical(x, y, z)
        print(empiricalJointPDF)
        print(str(theoreticalJointPDF) + "\n")

    # empirical_E = statistics.mean([v[2] for v in vectors])
    # theoretical_E = 1/8

    # empirical_var = statistics.variance([v[2] for v in vectors])
    # theoretical_var = 37/1728

    # print(f"Difference in Expectaton: {empirical_E-theoretical_E}")
    # print(f"Difference in Var: {empirical_var-theoretical_var}")

    # fname = "file_output.txt"
    # file = open(fname, "w")

    # file.write(f"x\tF_L1(x)\tF_L2(x)\tF_L3(x)\n")
    # for i in range(101):
    #     x = i/100
    #     FL1 = len([v for v in vectors if v[0]<=x])/len(vectors)
    #     FL2 = len([v for v in vectors if v[1]<=x])/len(vectors)
    #     FL3 = len([v for v in vectors if v[2]<=x])/len(vectors)
    #     file.write(f"{x}\t{FL1}\t{FL2}\t{FL3}\n")

    # file.close()