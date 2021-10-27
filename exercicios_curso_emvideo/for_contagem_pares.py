"""
Create a program that show on the screen all even numbers from 1 to 50
"""
for n in range(1, 51):  # we are iterating through the whole range
    if n % 2 == 0:
        print(n)


for i in range(2, 51, 2):  # in this for we iterate only through half of the list!
    print(i)
