
# Program to calculate Simple Interest

import sys
principal = int(sys.argv[1])
rate = int(sys.argv[2])
time = int(sys.argv[3])

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)
