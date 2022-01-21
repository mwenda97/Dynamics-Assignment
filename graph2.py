import matplotlib.pyplot as plt


x = [ 40,45,50,55,60]
y = [ -0.964140929,-2.411841814,-1.835210658,-1.4444,-0.44]


plt.title('Q2 input against errors')
plt.xlabel('input')
plt.ylabel('error')
plt.scatter(x,y)
plt.plot(x,y)
plt.show()