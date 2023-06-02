import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

if dice1 + dice2 == 7:
    print(f"{dice1}, {dice2} : 이겼습니다!")
else:
    print(f"{dice1}, {dice2} : 졌습니다.")