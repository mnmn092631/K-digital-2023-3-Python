# 1~n까지의 합을 계산하는 함수
def sum(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result
print(sum(100))

# 반지름을 전달하면 원의 면적을 반환하는 cir_area(r) 함수와 
# 원의 둘레를 반환하는 cir_cirm(r) 함수를 작성하라. 
# 이들 함수를 이용하여 반지름이 3.5cm인 원의 면적과 둘레를 
# 소수점 아래 첫 자리까지 구하라.
import math

def cir_area(r):
    return r ** 2 * math.pi

def cir_cirm(r):
    return r * 2 * math.pi

print(f"반지름이 3.5cm인 원의 면적 : {cir_area(3.5):.1f}")
print(f"반지름이 3.5cm인 원의 둘레 : {cir_cirm(3.5):.1f}")

# den(n) 함수를 이용하여 약수를 구하여 반환하는 프로그램을 작성
def den(n):
    result3 = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result3.add(i)
            result3.add(n // i)
    return sorted(result3)

print(f"12의 약수는 {den(12)}입니다.")