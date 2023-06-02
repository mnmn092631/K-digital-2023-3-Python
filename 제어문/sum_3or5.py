n = int(input("양의 정수를 입력해주세요"))
sum = 0

for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print(f"1부터 {n}까지의 자연수 중에서 3의 배수와 5의 배수의 합: {sum}")