# 사용자로부터 cm 단위의 길이를 입력 받는다.
# 입력 값이 음수이면 "잘못 입력하였습니다"라는 메시지를 출력하고 
# 양수이면 길이를 인치로 변환하여 출력하는 프로그램을 작성하라. 1인치 = 2.54cm
cm = float(input("cm 단위의 길이를 입력해주세요: "))
if cm < 0:
    print("잘못 입력하였습니다.")
else:
    print(f"{cm / 2.54}inch")

# 사용자로부터 이수한 학점을 입력 받는다. 
# 학점이 40학점 미만이면 "1학년입니다"를 출력하고, 
# 40이상 80미만이면 "2학년입니다"를 출력한다. 
# 학점이 80이상이면 "졸업반입니다"를 출력하는 프로그램을 작성하라.
inp = int(input("이수한 학점을 입력해주세요: "))
grade = "졸업반입니다." if inp >= 80 else ("2학년입니다." if inp >= 40 else "1학년입니다.")
print(grade)

# 사용자로부터 현재 시간을 나타내는 1~12의 숫자를 입력 받는다.
# 또 "am" 혹은 "pm"을 입력 받고 경과 시간을 나타내는 값을 입력 받는다. 
# 이로부터 최종 시간이 몇 시인지 출력하는 프로그램을 작성하라.
h = int(input("현재 시를 입력해주세요(1~12): "))
sel = input("오전 오후를 선택해주세요(1. am | 2. pm): ")
elap = int(input("경과 시간을 입력해주세요: "))

now = (h + elap) % 12

if now == 0:
    now = 12

if (h + elap) // 12 % 2 == 1:
    if sel == "1":
        sel = "pm"
    else: sel = "pm"

print(f"{now} {sel}")

# if now > 12:
#     now %= 12
#     if sel == "1":
#         print(f"{now} pm")
#     elif sel == "2":
#         print(f"{now} am")
# else:
#     if sel == "1":
#         print(f"{now} am")
#     elif sel == "2":
#         print(f"{now} pm")