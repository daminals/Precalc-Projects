# fib.py
# fibonacci sequence
# Daniel Kogan, 6/24/2020

def main():
    def fib_sequence(n):
        if n == 1:
            return 1
        elif n == 0:
            return 0
        else:
            return fib_sequence(n-1) + fib_sequence(n-2)

    def sequence_func(index):
        seq = []
        for i in range(index):
            seq.append(fib_sequence(i))
        return seq


    print(sequence_func(15))

if __name__ == '__main__':
    main()