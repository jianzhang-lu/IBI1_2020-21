import matplotlib.pyplot as plt
import numpy as np
gene_lengths=np.array([9410,394141,4442,105338,19149,76779,126550,36296,842,15981])
#use np.array to create a list
exon_counts=np.array([51,1142,42,216,25,650,32533,57,1,523])
#use np.array to create a list
average_axon_length=gene_lengths/exon_counts
#the two lists can perform four operations directly
average_axon_length.sort()
#sort the list from the smallest to the largest
print(average_axon_length)
#print the new list
plt.boxplot(average_axon_length,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=True)
#make a boxplot
plt.title('average_axon_length')
#add a title
plt.show()






