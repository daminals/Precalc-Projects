# fib.py
# fibonacci sequence
# Daniel Kogan, 6/24/2020

def main():
    def eff_fib_seq(n):  # Fibonacci sequence utilizing dynamic programming
        values = [0, 1]
        while len(values) < n:
            values.append(values[-1] + values[-2])
        return values

    def fib_sequence(n):  # Fibonacci sequence utilizing recursion
        if n == 1:
            return 1
        elif n == 0:
            return 0
        else:
            return fib_sequence(n - 1) + fib_sequence(n - 2)

    def sequence_func(index):  # Places the inefficient fibonacci sequence calcution into an array
        seq = []
        for i in range(index):
            seq.append(fib_sequence(i))
        return seq

    print(eff_fib_seq(1000))
    #print(sequence_func(50))


if __name__ == '__main__':
    main()
