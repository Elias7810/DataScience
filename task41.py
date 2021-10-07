from sys import argv

print(argv)
hours = int(argv[1])
rate = int(argv[2])
premium = int(argv[3])
wage = hours * rate + premium
print(wage)
