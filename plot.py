import matplotlib.pyplot as plt
a= [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
plt.xlabel("integer")
plt.ylabel("even int")
plt.title("Linear Graph")
# plt.plot(a,b, color='red')
food=["meat", "beans","tomato","avocado" ]
cal=[250,50,19,140]
k=[40,26,20,20]
fat=[8,2,2.5,3]
plt.xlabel("Food Types")
plt.ylabel("Nutrition")
# plt.plot(food, cal, label="calories")
# plt.plot(food, k, label="Potassium")
# plt.plot(food, fat, label="Fat")
# plt.legend()
# plt.grid()
plt.bar(food, cal)



plt.show()