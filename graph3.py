import matplotlib.pyplot as plt


x = [0.6534,14.63,34.58,56.86,78.36,96.85,111.2,121.1,127.3

 ]
y = [1.034,3.93,7.465,10.42,11.94,11.72,10.03,7.617,4.943

]


plt.title('series dc machine torque against speed graph')
plt.xlabel('speed(w)')
plt.ylabel("torque(n-m)")
plt.scatter(x,y)
plt.plot(x,y)
plt.show()