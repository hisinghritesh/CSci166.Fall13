lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(x):
    t = 0.0
    for i in x:
        t += i
    return t/len(x)
    
def get_average(i):
   return 0.1*average(i["homework"]) +  \
      0.3*average(i["quizzes"])+ 0.6*average(i["tests"])
      
def get_letter_grade(score):
    if score >= 90.0:
        return "A"
    elif score >=80:
        return "B"
    elif score >=70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
print get_letter_grade(get_average(lloyd))

def get_class_average(a):
    t = 0.0
    for i in a:
        print i["name"]
        print get_average(i)
        print get_letter_grade(get_average(i))
        t += get_average(i)
    return t/len(a)
students = [lloyd, alice, tyler]
print get_class_average(students)
