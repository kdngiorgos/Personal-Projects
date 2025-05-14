import math
import random

def pi_monte_carlo(num_samples):
    inside_circle = 0
    for i in range(100):
        for _ in range(num_samples):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            if x**2 + y**2 <= 1:
                inside_circle += 1
        print( str(i) + "%" )
    return (inside_circle / num_samples) * 0.04

print("How many samples do you want to use?")
num_samples = int(input())
print("Calculating pi using Monte Carlo method...")
pi_estimate = pi_monte_carlo(num_samples)
print(f"Estimated value of pi: {pi_estimate}")
print(f"Actual value of pi: {math.pi}")