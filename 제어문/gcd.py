a = int(input("첫번째 양의 정수를 입력해주세요 : "))
b = int(input("두번째 양의 정수를 입력해주세요 : "))

max = max(a, b)
min = min(a, b)
while min > 0:
    remain = max % min
    max = min
    min = remain

print(f"{a}, {b}의 최대공약수는 {max}입니다.")