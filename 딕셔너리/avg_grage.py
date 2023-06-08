students = {
    "Alice": [85, 90, 95],
    "Bob": [75, 80, 85],
    "Charlie": [95, 95, 95]
}

print("Average grades : ")
for s in students:
    print(f"{s}: {sum(students[s])/len(students[s])}")