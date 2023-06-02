list = []

for i in range(5):
    list.append(int(input(f"{i+1}번째 숫자를 입력해주세요(1~100)")))

print("[결과]")
print(f"입력받은 숫자들: {list}")

print(f"최댓값: {max(list)}\n최솟값: {min(list)}")
