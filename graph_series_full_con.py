import matplotlib.pyplot as plt

x = [2.024,1.993,1.903,1.766,1.6,1.423,1.335,1.191,1.078,1.009
    ]

y = [49.61,48.37,44.69,38.96,31.73,23.7,20.28,13.35,7.419,3.544
    
    ]
plt.xlabel('speed(w)')
plt.ylabel('torque(n-m)')
plt.title('single phase full convertor drive for series motor')
plt.scatter(x,y)
plt.plot(x,y)
plt.show()
