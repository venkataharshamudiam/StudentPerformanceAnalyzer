import pandas as pd
from src.analysis import calculate_averages

data = pd.read_csv("data/students.csv")

data = calculate_averages(data)

print(data)
print("Student report on main branch")
print("Student report feature")
