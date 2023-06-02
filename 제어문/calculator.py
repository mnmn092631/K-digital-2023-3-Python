while True:
    numA = input("첫 번째 수를 입력하세요 ('exit' 입력 시 종료) : ")
    if numA == "exit":
        break
    elif not str.isdigit(numA):
        print("올바른 값을 입력하세요.")
        continue
    numA = int(numA)

    numB = input("두 번째 수를 입력하세요 : ")
    if not str.isdigit(numB) :
        print("올바른 값을 입력하세요.")
        continue
    numB = int(numB)

    oper = input("연산자를 입력하세요 (+, -, *, /) : ")
    if oper == "+":
        result = numA + numB
    elif oper == "-":
        result = numA - numB
    elif oper == "*":
        result = numA * numB
    elif oper =="/":
        if numB == 0:
            print("0으로 나눌 수 없습니다")
            continue
        result = int(numA / numB)
    else :
        print("연산자를 잘못 입력하였습니다.")
        continue
    
    print(f"{numA} {oper} {numB} = {result}")