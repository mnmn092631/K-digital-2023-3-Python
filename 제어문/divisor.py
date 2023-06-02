num = int(input("양의 정수를 입력해주세요 : "))

print(f"{num}의 약수는 ", end="")
for i in range(1, num + 1):
    if num % i == 0:
        print(f"{i}", end=" ")
print("입니다.")