import matplotlib.pyplot as plt
plt.style.use('seaborn')
x_values = range(1,1000)
y_values = [x**2 for x in x_values]

#squares = [0,1,4,9,16,25]
#add = [1,2,3,4,5,6,7]
fig,ax = plt.subplots()
ax.scatter(x_values,y_values,s=10,c= y_values, cmap=plt.cm.Reds)
ax.set_title("lqx", fontsize = 24)
plt.savefig('lqx.png', bbox_inches = 'tight')