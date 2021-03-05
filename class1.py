import csv
import statistics
import pandas as pd
import plotly_express as px

with open("class1.csv",newline="") as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)

newData = []

for i in range(len(fileData)):
    num = fileData[i][1]
    newData.append(float(num))

n = len(newData)
total = 0

for x in newData:
    total = total + x

mean = total/n
print(mean)

df = pd.read_csv("class1.csv")

fig = px.scatter(df,x = "Student Number", y = "Marks")

fig.update_layout(shapes = [dict(type = "line",y0 = mean, y1 = mean, x0 = 0, x1 = n)])
fig.update_yaxes(rangemode = "tozero")
fig.show()