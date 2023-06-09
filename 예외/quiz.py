data = { "Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6 }

# try-except를 이용하지 않음
while True:
    s = input("문자열을 입력해주세요 : ")
    if s in data:
        print(data[s])
    else:
        print("항목이 없습니다.")
        break
    
# try-except를 이용
try:
    while True:
        s = input("문자열을 입력해주세요 : ")
        print(data[s])
except:
    print("항목이 없습니다.")