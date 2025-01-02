import re

with open('03_input.txt') as f:
    data = f.read()

mults = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)
print(mults)

sum = 0
for x, y in mults:
    sum += int(x) * int(y)

print(sum)
