import random

findNum = random.randint(1, 100)

print("[1 ~ 100 사이의 숫자 맞추기]")
for i in range(1, 5 + 1):
    inNum = int(input(f"{i}번째 시도(1 ~ 100 입력) : "))
    if findNum == inNum:
        print("정답입니다!")
        break
    elif findNum < inNum:
        print(f"{inNum}보다 작은 숫자입니다.")
    else:
        print(f"{inNum}보다 큰 숫자 입니다.")