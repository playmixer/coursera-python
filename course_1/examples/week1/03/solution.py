import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

x1 = (-b + (b*b - 4 * a * c)**(1/2))/(2 * a)
x2 = (-b - (b*b - 4 * a * c)**(1/2))/(2 * a)
print(int(x1))
print(int(x2))
