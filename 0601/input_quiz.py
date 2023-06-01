count = int(input("사과의 개수를 입력해주세요.: "))
price = int(input("사과의 가격을 입력해주세요.: "))
vat = float(input("부가세율을 입력해주세요.: "))

print(f"총 가격은 {int(count * price * (1 + vat))}원입니다.")