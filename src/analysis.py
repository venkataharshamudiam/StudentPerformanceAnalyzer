import pandas as pd


def calculate_averages(data):
    data["Average"] = data[["Maths", "Science", "English"]].mean(axis=1)
    return data


def find_top_student(data):
    return data.loc[data["Average"].idxmax()]