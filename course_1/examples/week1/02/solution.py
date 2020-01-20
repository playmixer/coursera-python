import sys

digit_string = int(sys.argv[1])
for i in range(digit_string,-1,-1):
    if i < digit_string:
        print(' '*i, '#'*(digit_string-i), sep='')
