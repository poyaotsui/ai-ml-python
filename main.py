import pandas as pd #read data
import matplotlib.pyplot as plt #for drawing out data
#from ipywidgets import interact #only works on jupyter so gotta do python3 -m pip install notebook
#jupyter notebook

#https://www.youtube.com/watch?v=wm9yR1VspPs&t=1239s
#
#
#simple linear regression
'''
how to find the perfect slope on a given graph : y=mx+b
'''
url = "https://raw.githubusercontent.com/GrandmaCan/ML/main/Resgression/Salary_Data.csv"
data = pd.read_csv(url)
print(data)
# y = m x + b <- using this formula to predict the y using x

x=data["YearsExperience"]
y = data["Salary"] #<- the true y

print(x)
print("-----------------")
print(y)
'''
plt.scatter(x,y, marker="x", color="red") #marker , color changes the appearance on the graph
plt.title("years of experience to salary")
plt.xlabel("years of experience")
plt.ylabel("salary (thousands"))
plt.show()
'''




def plot_pred(w,b):
    #b controls the up and down of the bar
    #w controls how much the line tilts
    y_pred = x*w+b
    plt.plot(x,y_pred, color="blue", label="prediction line")# draws line
    plt.scatter(x,y, marker="x", color="red",label ="real data") #draws the scatterplot
    plt.title("years of experience to salary")
    plt.xlabel("years of experience")
    plt.ylabel("salary (thousands")
    plt.xlim([0,12])
    plt.ylim([-60,140])
    plt.legend()
    plt.show()


#interact(plot_pred, w=(-100,100,1),b=(-100,100,1)) only works in jupyter
plot_pred(1,0)
#34.05

#how to find the perfect line
#look at the variables and calculate the distance from the variabel to the line and find the closest one
#
#
