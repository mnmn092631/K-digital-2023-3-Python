# My name is -Tom- and I am -20- years old.
name = "Tom"
age = 20
# %
print("My name is %s and I am %d years old." % (name, age))
# format()
print("My name is {} and I am {} years old.".format(name, age))
# f-string
print(f"My name is {name} and I am {age} years old.")

# I have -3- apples, -2- oranges, and -1- banana
apples = 3
oranges = 2
banana = 1
# %
print("I have %d apples, %d oranges, and %d banana." % (apples, oranges, banana))
# format()
print("I have {} apples, {} oranges, and {} banana.".format(apples, oranges, banana))
# f-string
print(f"I have {apples} apples, {oranges} oranges, and {banana} banana.")

# The result is -1.23-.
result = 1.23
# %
print("The result is %.2f." % result)
# format()
print("The result is {:.2f}.".format(result))
# f-string
print(f"The result is {result:.2f}.")

# Your score is -90-%
score = 90
# %
print("Your score is %d%%." % score)
# format()
print("Your score is {}%.".format(score))
# f-string
print(f"Your score is {score}%.")

# -10- + -20- = -30-
a = 10
b = 20
c = 30
# %
print("%d + %d = %d" % (a, b, c))
# format()
print("{} + {} = {}".format(a, b, c))
# f-string
print(f"{a} + {b} = {c}")