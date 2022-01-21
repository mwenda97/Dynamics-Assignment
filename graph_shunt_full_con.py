import matplotlib.pyplot as plt

x = [18.47,18.22,17.44,16.2,14.53,12.5,10.18,7.645
    ]

y = [480.8,475.4,458.4,430.1,390.1,339.5,278.6,209
    
    ]
plt.xlabel('speed(w)')
plt.ylabel('torque(n-m)')
plt.title('single phase full convertor drive for shunt motor')
plt.scatter(y,x)
plt.plot(y,x)
plt.show()
