import csv
import statistics
import pandas as pd
import math
import plotly_express as px

with open("classData.csv",newline="") as f:
    reader = csv.reader(f)
    fileData = list(reader)

data = fileData[0]

total = 0

n = len(data)

for x in data:
    total = total + int(x)

mean = total/n
print(mean)

list = []
for num in data:
    a = int(num)- mean
    a = a**2
    list.append(a)

sum = 0

for x in list:
    sum = sum + x

result = sum/(n-1)
standardDeviation = math.sqrt(result)
print(standardDeviation)