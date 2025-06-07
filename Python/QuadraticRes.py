import math
from collections import defaultdict


print("Modulo: ")
p = int(input())

qres = defaultdict(list)

for i in range(1, p):
    remainder = i**2 % p
    qres[remainder].append(i) 

sorted_hashmap = {k: qres[k] for k in sorted(qres)}    

print(f"Quadratic residues modulo {p}:")
print(f"{sorted_hashmap}")