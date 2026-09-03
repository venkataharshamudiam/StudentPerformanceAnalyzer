print("Student Performance Analyzer")
print("My first real Git project!")
import csv

students = []

with open("data/students.csv", "r") as file:
    reader = csv.DictReader(file)

    for student in reader:
        maths = int(student["Maths"])
        science = int(student["Science"])
        english = int(student["English"])

        average = (maths + science + english) / 3

        students.append({
            "Name": student["Name"],
            "Average": average
        })

        print(student["Name"], "Average:", round(average, 2))

top_student = max(students, key=lambda student: student["Average"])

print("\nTop Student:", top_student["Name"])
print("Highest Average:", round(top_student["Average"], 2))