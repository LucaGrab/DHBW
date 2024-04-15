#Bar
xLabels = ['A','B','C','D']
plt.bar(xLabels,yPoints, width=0.2)
plt.show()

#Pie
myexplode = [0.3, 0, 0, 0]
#plt.pie([2,5,3,10], labels=xLabels)
plt.pie([2,5,3,10], labels=xLabels, startangle = 90, explode=myexplode)

plt.show()
#Startet bei der X-Achse und zeichnet gegen den Uhrzeigersinn

x = np.random.normal(170, 10, 10000000)
plt.hist(x)
plt.show()