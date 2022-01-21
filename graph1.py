import matplotlib.pyplot as plt


x = [15.33,32.9,48.53,62.61,75,86.07,96.36,106.2,116.9

 ]
y = [2.428,4.095,5.307,6.063,6.439,6.274,5.775,4.802,3.164

]


plt.title('separately excited dc machine torque against speed graph')
plt.xlabel('speed(w)')
plt.ylabel("torque(n-m)")
plt.scatter(x,y)
plt.plot(x,y)
plt.show()
