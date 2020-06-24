# permutations.py
# finds all possible combinations of a string
# Daniel Kogan, 6/24/2020

from math import *

def main():
    def permutations(str):
        if str == '':
            return['']
        all_perms=[]
        for char in str:
            subpermutations = permutations(str.replace(char,'',1))
            for each in subpermutations:
                all_perms.append(char+each)
        return all_perms

    print(permutations('stinky'))

if __name__ == '__main__':
    main()