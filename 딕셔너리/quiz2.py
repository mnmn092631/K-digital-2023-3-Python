d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
  {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
  {'name':'Princess', 'phone':'555-3141', 'email':''},
  {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

print("전화번호가 8로 끝나는 사용자 이름을 출력")
for item in d:
    if(item["phone"][-1] == "8"):
        print(item["name"])

print("이메일이 없는 사용자 이름을 출력")
for item in d:
    if(item["email"] == ""):
        print(item["name"])

name = input("사용자 이름을 입력해주세요 : ")
flag = False
for item in d:
    if(item["name"] == name):
        flag = True
        print(f"{name}의 전화번호는 {item['phone']}, 이메일은 {item['email']}입니다.") 
if(not flag):
    print("이름이 없습니다.")