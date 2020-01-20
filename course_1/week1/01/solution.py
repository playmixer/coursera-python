import sys

digit_string = sys.argv[1]

total = 0
for n in digit_string:
    total += int(n)
print(total)
