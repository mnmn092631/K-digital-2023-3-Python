print("사과의 개수를 입력해주세요.")
count = int(input())
print("사과의 가격을 입력해주세요.")
price = int(input())
print("부가세율을 입력해주세요.")
vat = float(input())

print(f"총 가격은 {int(count * price * (1 + vat))}원입니다.")