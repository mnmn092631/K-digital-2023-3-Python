days = {'January':31, 'February':28, 'March':31, 'April':30,
        'May':31, 'June':30, 'July':31, 'August':31,
        'September':30, 'October':31, 'November':30, 'December':31}

month = input("월을 입력해주세요(ex. January) : ")
print(f"{month}는 {days.get(month)}일까지 있습니다.")

print(sorted(days.keys()))

print("일수가 31인 모든 월을 출력")
for m in days:
    if(days[m] == 31):
        print(m)

print("월의 일수를 기준으로 오름차순으로 key-value 쌍을 출력")
for k, v in sorted(days.items(), key=lambda x : x[1]):
    print(k)

m3 = input("월을 3자리만 입력해주세요(ex. Jan) : ")
for m in days:
    if(m.startswith(m3)):
        print(f"{m}는 {days[m]}일까지 있습니다.")