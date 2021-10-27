"""
Create a code that calculates the sum of all odd numbers that are multiples of 3 in the interval [1,500]
"""

sum = 0
count = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        sum += i
        count += 1

print(f'There are {count} multiples of 3 between 1 and 500 and they sum to {sum}')
