# enumerate() 내장 함수를 이용하여 
# 사용자가 입력한 문자열에서 'a' 문자의 위치를 모두 찾아 출력하는 프로그램을 작성하라.
# 'a'가 없으면 "a가 없습니다'라는 메시지를 출력하라.
str = input("알파벳으로 구성된 문자열을 입력해주세요 : ")
for i, c in enumerate(str, start=0):
    if(c == "a"):
        print(i, end=", ")
print()

# 두 수의 합(sum), 차(sub), 곱(mul), 나누기(div)를 수행하는 함수를 각각 정의하라.
# 딕셔너리를 이용하여 사용자가 '1'을 입력하면 sum()을 호출하고,
# '2'를 입력하면 sub(),
# '3'을 입력하면 mul(), 
# '4'를 입력하면 div() 함수를 호출하여 두 수의 연산을 수행하는 프로그램을 작성하라.
def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if (b == 0):
        "0으로 나눌 수 없습니다."
    return a / b

dic = {"1" : sum, "2" : sub, "3" : mul, "4" : div}
num1 = int(input("첫번째 수 입력 : "))
num2 = int(input("두번째 수 입력 : "))
op = input("연산 입력(1. sum, 2. sub, 3. mul, 4. div) : ")

func = dic[op]
print(func(num1, num2))

# 다음과 같이 구성되는 문자열을 구분 문자(&, =)로 분리하여 
# 딕셔너리로 반환하는 함수 작성
# 예: 문자열 'led=on&motor=off&switch=off'이고 구분 문자가 '&', '='일 때
# {'led':'on', 'motor':'off', 'switch':off'} 반환.
# Hint: dict([['a','b'], ['c', 'd']]) -> {'a': 'b', 'c': 'd'}
def split_str(s):
    result = []
    list_s = s.split("&")
    for item in list_s:
        result.append(item.split("="))
    return dict(result)

print(split_str("led=on&motor=off&switch=off"))
