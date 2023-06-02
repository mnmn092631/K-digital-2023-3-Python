from random import randint

coin = 50

while 0 < coin and coin < 100:
    choice = int(input("앞면 또는 뒷면을 골라주세요(1. 앞면 | 2. 뒷면) : "))
    side = randint(1, 2)
    if choice == side:
        coin += 9
        print(f"일치합니다! 현재 금액 : {coin}")
    else:
        coin -= 10
        print(f"틀렸습니다. 현재 금액 : {coin}")