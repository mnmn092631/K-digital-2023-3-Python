class People :
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name

    def introMe(self):
        print("Name :", self.__name, "age :", str(self.__age))
    
    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__name
    
    def set_age(self, age):
        if (age <= 0):
            return print("잘못된 나이입니다.")
        self.__age = age
    
    def set_name(self, name):
        self.__name = name

class Teacher(People) :
    def __init__(self, age=0, name=None, school=None) :
        super().__init__(age, name)
        self.school = school

    def showSchool(self):
        print("My School is ", self.school)

t = Teacher(36, "Kim", 'High School')
t.introMe()
t.showSchool()
print("-" * 30)

t.set_name("Lee")
t.set_age(47)
t.introMe()
print("-" * 30)