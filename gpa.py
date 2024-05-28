"""
This program allows the user to calculate their cgpa
"""
number_of_courses = int(input("Enter number of courses offered:\n"))
courses = []
list_of_product_of_grade_and_unit = []
uni = []
units = {
    "course code":["unit", "grade score","total"]
}

def numberOfCoursesOffered():
    for num in range(number_of_courses):
        course = input("course name:\n")
        courses.append(course)

def assignUnitAndGradeToCourse():
    for course in courses:
        unit = int(input(f"Enter unit for course {course}:\n"))
        units[course] = []
        units[course].append(unit)
        grade = int(input(f"Enter grade score for course {course}:\n"))
        units[course].append(grade)

def storeProductofguAndUnit():
    for course in courses:
        product_of_grade_and_unit = units[course][0] * units[course][1]
        un = units[course][0]
        uni.append(un)
        list_of_product_of_grade_and_unit.append(product_of_grade_and_unit)

def calculateGpa():
    total_units = sum(uni)
    total_of_product_of_grade_and_unit = sum(list_of_product_of_grade_and_unit)
    gpa = total_of_product_of_grade_and_unit/total_units
    print(f"gpa is {gpa}")

numberOfCoursesOffered()
assignUnitAndGradeToCourse()
storeProductofguAndUnit()
calculateGpa()
