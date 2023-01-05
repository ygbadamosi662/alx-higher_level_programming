#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    from calculator_1.py import add,div,sub,mul

    count = len(sys.argv[1:])
    lik = ['+', '-', '/', '*']
    hi = false

    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    for i in range(len(lik)):
        if lik[i] == sys.argv[2]:
            hi = true
            break
    if hi == false:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = sys.argv[1]
    b = sys.argv[3]

    if sys.argv[2] == '+':
        print('{0} {1} {2} = {3}'.format(a, sys.argv[2], b, add(int(a), 
            int(b))))
    elif sys.argv[2] == '-':
        print('{0} {1} {2} = {3}'.format(a, sys.argv[2], b, sub(int(a), 
            int(b))))
    elif sys.argv[2] == '/':
        print('{0} {1} {2} = {3}'.format(a, sys.argv[2], b, div(int(a), 
            int(b))))
    elif sys.argv[2] == '*':
        print('{0} {1} {2} = {3}'.format(a, sys.argv[2], b, mul(int(a), 
            int(b))))
