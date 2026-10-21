import pandas as pd #read data
import matplotlib.pyplot as plt #for drawing out data
import numpy as np
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
'''



#how to find the perfect line
# - cost function => cost = (real value - predictino value)^2
#look at the variables and calculate the distance from the variabel to the line and find the closest one
#
#cost function
#
#
def compute_cost(x,y,w,b):
    y_pred= w*x+b
    cost = (y-y_pred)**2
    cost=cost.sum()/len(x)
    return cost


print(compute_cost(x,y,10,10))

#what is the cost if b=0 w=-100~100
costs=[]
for w in range(-100,101):
    cost=compute_cost(x,y,w,0)
    costs.append(cost)

print(costs)

#plt.scatter(range(-100,101),costs)
plt.plot(range(-100,101),costs)
plt.title("cost function b=0,w=-100~100")
plt.xlabel("w")
plt.ylabel("cost")
plt.show()

#the cost if w=-100~100 b=-100~100
print("----------------")
ws=np.arange(-100,101)
bs=np.arange(-100,101)

costs= np.zeros((201,201))

i=0
for w in ws:
    j=0
    for b in bs:
        cost = compute_cost(x,y,w,b)
        costs[i,j]= cost
        j=j+1
    i=i+1

print(costs)

ax=plt.axes(projection="3d")
ax.xaxis.set_pane_color((0,0,0))
ax.yaxis.set_pane_color((0,0,0))
ax.zaxis.set_pane_color((0,0,0))

b_grid,w_grid=np.meshgrid(bs,ws)
ax.plot_surface(w_grid,b_grid,costs)

ax.set_title("w b cost")

plt.show()
#52.25
