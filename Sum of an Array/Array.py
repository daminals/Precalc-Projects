# Array Shenanigans
# Verifying the formula (n(n-1))/2 is the same as adding all of the items of an array where the
# items increase by 1
# 5/25/2020

counter = 1
while True:
    counter += 1  # Fewer than two items in the array breaks the system

    n = range(1, counter)  # Creates an array with every integer between 1(inclusive) and 101(exclusive)

    Manual_solution = 0
    for items in n:
        Manual_solution += items  # Manually adds our array items

    Solution = (n[0] + n[len(n) - 1]) * (len(n) / 2)

    # print(Manual_solution)
    # print(Solution)

    print(Manual_solution == Solution)
