#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

n = 5

sum = 0 
for i in range(1,(5+1)):
 sum += i

fac = 1
for i in range(1, (5+1)):
 fac *= i
 print(n, sum, fac)
