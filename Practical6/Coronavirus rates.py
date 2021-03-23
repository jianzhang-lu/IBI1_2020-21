
# import packages.
import numpy as np
import matplotlib.pyplot as plt
# create a dictionary to store data
dict_of_cases = {"USA": 29862124, "India": 11285561,
                 "Brazil": 11205972, "Russia": 4360823,
                 "UK": 4234924}
# print the dictionary
print(dict_of_cases)
#output the sizes and labels using .keys/.values
sizes=dict_of_cases.values()
labels =dict_of_cases.keys()
explode=(0.1,0,0,0,0)
# draw the pie chart
plt.pie(sizes, explode=explode, labels=labels, shadow=False, autopct='%1.1f%%')
#add a title
plt.title("Coronavirus Infection Rates across Countries")
plt.legend()
#show the pie
plt.show()
