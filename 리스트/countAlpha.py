text = "Hello, world!"
count = {}

for c in text:
    if(c in count):
        count[c] += 1
    else:
        count[c] = 1

print(count)