# 사용자가 입력한 문자열에 대해 다음 물음에 답하라
inStr = input("문자열을 입력해주세요 : ")
# 문자열의 문자수를 출력하라
print(f"문자열의 문자수는 {len(inStr)}입니다.")
# 문자열을 10번 반복한 문자열을 출력하라
print(inStr * 10)
# 문자열의 첫 번째 문자를 출력하라
print(f"첫 번째 문자는 {inStr[0]}입니다.")
# 문자열에서 처음 3문자를 출력하라
print(inStr[:3])
# 문자열에서 마지막 3문자를 출력하라
print(inStr[len(inStr) - 3:len(inStr)])
# 문자열의 문자를 거꾸로 출력하라
print(inStr[::-1])
# 문자열에 7번째 문자가 있으면 출력하고 없으면 '문자가 없습니다'라는 메시지를 출력하라
if len(inStr) < 7 :
    print("문자가 없습니다.")
else:
    print(f"7번째 문자는 {inStr[6]}입니다.")
# 문자열에서 첫 번째 문자와 마지막 문자를 제거한 문자열을 출력하라
print(inStr[1:len(inStr) - 1])
# 문자를 모두 대문자로 변경하여 출력하라
print(inStr.upper())
# 문자를 모두 소문자로 변경하여 출력하라
print(inStr.lower())
# 문자열에서 'a'를 'e'로 대체하여 출력하라
print(inStr.replace("a", "e"))
