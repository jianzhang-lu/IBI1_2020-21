import matplotlib.pyplot as plt
x={'USA':29862124, 'Inida':11285561, 'Brazil':11205972, 'Russia':4360823, 'UK':4234924}
# create a dictionary to include all data
labels=x.keys()
# create labels to represent all keys in dictionary 'x'.
sizes=x.values()
# create sizes to represent all values in dictionary 'x'
explode=[0.1,0,0,0,0]
# explode one of the countries to make it take apart from the circle.
plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', startangle=90)
# make the pie and let its sizes be values of x and let lebels be keys of x.
plt.axis('equal')
# to make the pie look like a circle
plt.legend()
# add a legend for a better pie
plt.title("Coronavirus_rates")
# the name of the pie
plt.show()
# to see the pie
print(x) 
# print the dictionary 