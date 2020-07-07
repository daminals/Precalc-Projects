# ShiftChar.py
# Shifts a string by x amount
# Daniel Kogan, 6/24/2020

def main():

    def Shift(str,char):
        if char >= 0:
            for i in range(char):
                str = str[-1] + str[:-1]
        else:
            for i in range(abs(char)):
                str = str[1:] + str[0]
        return str

    def Shift_rec(str,char):
        if char==0:
            return str
        if char > 0:
            return Shift_rec(str[-1]+str[:-1],char-1)
        else:
            return Shift_rec(str[1:] + str[0],char+1)

    print(Shift('abcd',3))
    print(Shift_rec('abcd',3))

if __name__ == '__main__':
    main()