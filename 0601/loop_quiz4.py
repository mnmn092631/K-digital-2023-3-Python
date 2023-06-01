num = int(input("피보나치 수열의 몇 번째 항을 출력할까요?(1 이상의 양의 정수)"))

result = 1
next = 1
for i in range(num - 1):
    result, next = next, result + next


print(f"피보나치 수열의 {num}번째 항은 {result}입니다.")