import matplotlib.pyplot as plt
import numpy as np
# a= [1, 2, 3, 4, 5]
# b = [2, 4, 6, 8, 10]
# plt.xlabel("integer")
# plt.ylabel("even int")
# plt.title("Linear Graph")

# # plot
# plt.plot(a,b, color='red')

food=["meat", "beans","tomato","avocado" ]
cal=[25,30,19,40]
k=[40,26,20,20]
# fat=[8,2,2.5,3]
plt.xlabel("Food Types")
plt.ylabel("Nutrition")
# plt.plot(food, cal, label="calories")
# plt.plot(food, k, label="Potassium")
# plt.plot(food, fat, label="Fat")
# plt.legend()
# plt.grid()

# Bar
width=0.3
# n1=np.arange(len(food))  # [0,1,2,3]
# n2=[j+width for j in n1] # [0,1,2,3]
# plt.bar(n1,cal, width,label ="Calories")
# plt.bar(n2, k,width,label="potassium")
# plt.xticks(n1+width/2,food)
# plt.legend()

# hist 
p=[x for i in range(10, )]


plt.show()