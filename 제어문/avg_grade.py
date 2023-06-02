kor = int(input("국어 성적을 입력해주세요"))
eng = int(input("영어 성적을 입력해주세요"))
math = int(input("수학 성적을 입력해주세요"))

print("[성적 결과]")
print(f"국어: {kor}점, 영어: {eng}점, 수학: {math}점")

avg = kor * 0.4 + eng * 0.4 + math * 0.2
print(f"총 평균 점수: {avg:.2f}점")

grade = "A" if avg >= 90 else ("B" if avg >= 80 else ("C" if avg >= 70 else ("D" if avg >= 60 else "F")))
print(f"학점: {grade}")