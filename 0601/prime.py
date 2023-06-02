num = int(input("자연수를 입력해주세요 : "))

print(f"2부터 {num}까지의 소수는 ", end="")
for i in range(2, num + 1):
    isPrime = True
    for j in range(2, i):
        if i == 2:
          break
        if i % j == 0:
          isPrime = False
          break
    if isPrime:
      print(i, end=" ")
print("입니다.")