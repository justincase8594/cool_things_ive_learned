# taking values from a list can be a weird thing to think about.
# for loops are one of the most common ways to take values out of a list
# you can also make anothier list with a for loop and appending if the condition is True

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for i in a:
    if i < 5:
        b.append(i)
#print the result
print(b)
