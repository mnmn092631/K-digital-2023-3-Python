while True:
    score = int(input("점수를 입력해주세요(음수 입력시 종료) : "))
    if score < 0:
        print("종료합니다")
        break
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 60:
        print("C")
    elif score >= 40:
        print("D")
    else:
        print("F")