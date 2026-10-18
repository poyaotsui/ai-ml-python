import pandas as pd #read data
import matplotlib.pyplot as plt #for drawing out data
#https://www.youtube.com/watch?v=wm9yR1VspPs&t=1239s
#simple linear regression
'''
how to find the perfect slope on a given graph : y=mx+b
'''
url = "https://raw.githubusercontent.com/GrandmaCan/ML/main/Resgression/Salary_Data.csv"
data = pd.read_csv(url)
print(data)
# y = m x + b

x=data["YearsExperience"]
y = data["Salary"]

print(x)
print("-----------------")
print(y)

plt.scatter(x,y, marker="x", color="red") #marker , color changes the appearance on the graph
plt.title("years of experience to salary")

plt.show()
