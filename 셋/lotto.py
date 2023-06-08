import random

set = set()

while(len(set) < 6):
    n = random.randint(1, 45)
    set.add(n)

print(sorted(set))