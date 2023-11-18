import statistics
import numpy as np

trials = 2**20
vectors = []

for _ in range(trials):
    L1 = np.random.uniform(0,1)
    L2 = np.random.uniform(0,L1)
    L3 = np.random.uniform(0,L2)

    vectors.append((L1, L2, L3))

empirical_E = statistics.mean([v[2] for v in vectors])
theoretical_E = 1/8

empirical_var = statistics.variance([v[2] for v in vectors])
theoretical_var = 37/1728

print(f"Difference in Expectaton: {empirical_E-theoretical_E}")
print(f"Difference in Var: {empirical_var-theoretical_var}")

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