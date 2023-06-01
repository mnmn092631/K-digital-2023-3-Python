# % 연산자를 이용한 포매팅
name = "John"
age = 30
height = 175.5

print("My name is %s, I'm %d years old, and my height is %.1f." % (name, age, height))

num = 10
pi = 3.14159265

print("num = %d" % num)
print("pi = %f" % pi)
print("pi = %.2f" % pi)
print("pi = %10.2f" % pi)

# format() 메소드를 이용한 문자열 포매팅
print("My name is {}, I'm {} years old, and my height is {:.1f}.".format(name, age, height))

# f-string을 이용한 포매팅
print(f"My name is {name}, I'm {age} years old, and my height is {height:.1f}.")