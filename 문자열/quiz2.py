# 문자 'a'가 들어가는 단어를 키보드에서 입력 받아
# 첫 번째 줄에는 'a'까지의 문자열을 출력하고
# 두 번째 줄에는 나머지 문자열을 출력하는 프로그램을 작성하라.
inStr = input("문자 'a'가 들어가는 단어를 입력해주세요 : ")
aIdx = inStr.find("a")
print(inStr[:aIdx + 1])
print(inStr[aIdx + 1:])

# 숫자를 문자열로 변화하는 방법은 str(num)을 이용한다.
# str(12) '12'가 된다.
# 반대로 문자열을 숫자로 변환하려면 int(string)을 이용한다.
# int('12') 12가 된다.
# 이를 이용하여 1부터 1000까지의 숫자의 각 자리수의 합을 모두 구하라.
sum = 0
for i in range(1, 1000 + 1):
    s = str(i)
    for j in s:
        sum += int(j)
print(sum)