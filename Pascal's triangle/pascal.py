# pascal.py
# Deriving a recursive and explicit function for the sequence commonly referred to as Pascal's Triangle

def recursive_func(number_of_terms):
    n = [0, 1]  # First two terms of the sequence
    addition = [0, 1]  # First two numbers we add by, 0+1 = 1, 1+1 = 2

    for x in range(1, number_of_terms):
        new_add = addition[x] + 1 + x
        addition.append(new_add)  # Adds the additive number to the addition list
        new_dig = n[x] + new_add  # Calculate the New Digit of the sequence
        n.append(new_dig)  # Adds new term to the sequence

    #print(n[number_of_terms-1])  # Display the sequence
    return n[number_of_terms - 1]

# Due to the discovery made in deriving the explicit, we can theoretically increase efficiency
# by replacing the addition list with x(x+1)/2. However, this is flawed for the purposes of this
# program due to the fact that we need to solve for the previous term in a recursive formula,
# so looping through and finding all of the previous terms is what I did. Of course, we could solve
# for the previous term through the explicit formula, but that's kind of cheating 😕


def explicit_func(x):  # Where x is the subscript of n
    n = 0
    for i in range(x, 1, -1):
        i -= 1
        n += (i * (i + 1)) / 2
    #print(n)
    return n


def comparison(term_number):
    return recursive_func(term_number) == explicit_func(term_number)


for x in range(1, 100000):
    print(comparison(x))

#print([explicit_func(2),explicit_func(3),explicit_func(4),explicit_func(5),explicit_func(6),explicit_func(7)])