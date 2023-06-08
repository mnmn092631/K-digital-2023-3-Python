class Student:
    def __init__(self, name, student_id, year, major, avg_score):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.major = major
        self.avg_score = avg_score
    
    def get_info(self):
        return f"{self.name}({self.student_id}) : {self.year}학년, {self.major}전공 - 평균 성적 : {self.avg_score}"

class StudentManager:
    def __init__(self):
        self.student_list = []
    
    def add_student(self, student):
        self.student_list.append(student)
    
    def remove_student(self, student_id):
        for student in self.student_list:
            if(student_id == student.student_id):
                self.student_list.remove(student)
    
    def find_student(self, student_id):
        for student in self.student_list:
            if student_id == student.student_id:
                print(student.get_info())
    
    def show_all_students(self):
        for student in self.student_list:
            print(student.get_info())

student_manager = StudentManager()
student1 = Student("김", "00000000", 1, "가", 10)
student2 = Student("이", "00000001", 2, "나", 20)
student3 = Student("박", "00000002", 3, "다", 30)
student4 = Student("정", "00000003", 4, "라", 40)
student5 = Student("유", "00000004", 5, "마", 50)

student_manager.add_student(student1)
student_manager.add_student(student2)
student_manager.add_student(student3)
student_manager.add_student(student4)
student_manager.add_student(student5)

student_manager.remove_student("00000000")

print("학번으로 학생 찾기")
student_manager.find_student("00000001")
print()

print("모든 학생 출력 : ")
student_manager.show_all_students()