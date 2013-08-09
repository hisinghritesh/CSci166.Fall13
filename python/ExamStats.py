grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / len(grades)
    return average

def grades_variance(g, a):
    v = 0
    for i in g:
        v += (i-a)**2
    return v/len(g)

def grades_std_deviation(v):
    return v**(0.5)

v = grades_variance(grades, grades_average(grades))
print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades, grades_average(grades))
print grades_std_deviation(v)
