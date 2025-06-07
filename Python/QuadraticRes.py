import math
from collections import defaultdict

def BruteForce(p):
    hashmap = defaultdict(list)
    for i in range(1, p):
        remainder = i**2 % p
        hashmap[remainder].append(i) 
    return hashmap


def LegendreSymbol(a, p):
    if a == 0:
        return 0
    return pow(a, (p - 1) // 2, p)

def LegendreResidues(p):
    hashmap = defaultdict(list)
    for i in range(1, p):
        if LegendreSymbol(i, p) == 1:
            remainder = i**2 % p
            hashmap[remainder].append(i)
    return hashmap


def main():
    p = int(input("Enter a modulo p: "))
    ch = input("Do you want to use brute force (b) or Legendre (l) or Specific Integers (s)? ")
    
    sorted_hashmap = {}
    match ch:
        case 'b':
            qres = BruteForce(p)
            sorted_hashmap = {k: qres[k] for k in sorted(qres)}  
        case 'l':
            qres = LegendreResidues(p)
            sorted_hashmap = {k: qres[k] for k in sorted(qres)}
        case 's':
            while True:
                temp  = int(input("Give me a number):"))
                if temp < 0 or temp >= p:
                    print(f"Number must be in the range [0, {p-1}].")
                    break
                if LegendreSymbol(temp, p) == 1:
                    print(f"{temp} is a quadratic residue modulo {p}.")
    if sorted_hashmap:             
        print(f"Quadratic residues modulo {p}:")
        print(f"{sorted_hashmap}")


if __name__ == "__main__":
    main()