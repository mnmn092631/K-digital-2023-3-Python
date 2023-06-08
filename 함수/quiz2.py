# 두 개의 매개변수 n, m을 전달받아 m x n개의 * 상자를 출력하는 프로그램을 함수로 작성
def box(n, m):
    for _ in range(n):
        for _ in range(m):
            print("*", end="")
        print("")
box(2, 4)
print("-" * 10)

# 하나의 숫자를 전달받아 숫자의 자리 합을 구하는 함수를 작성
def sum_num(num):
    result = 0
    for n in str(num):
        result += int(n)
    return result

print(sum_num(123))
print("-" * 10)

# 두 개의 문자열이 서로 다른 처음 위치를 반환하는 함수를 작성. 두 개의 문자열이 같으면 -1을 반환
def idx(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    minlen = min(len1, len2)
    for i in range(minlen):
        if(str1[i] != str2[i]):
            return i
    if(len1 == len2):
        return -1
    else:
        return minlen

print(idx("hello", "hello"))
print(idx("hello", "hell"))
print(idx("hello", "helo"))
print("-" * 10)

# 문자열과 하나의 문자를 전달받아 문자열에서 문자의 위치를 모두 찾아 리스트로 반환하는 함수를 작성
def idx_char(str, c):
    idx_list = []
    for i in range(len(str)):
        if(c == str[i]):
            idx_list.append(i)
    return idx_list

print(idx_char("asdgciwaasxxaaa", "a"))
print("-" * 10)

# 재귀 함수를 이용하여 1부터 100까지의 합을 계산하는 프로그램
def sum(n):
    if (n == 1):
        return 1
    return n + sum(n - 1)

print(sum(100))