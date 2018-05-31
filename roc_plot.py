import numpy as np
import matplotlib.pyplot as plt

a=[]
b=[]
#data = np.genfromtxt('roc_test.dat',delimiter=' ')
#print data[1,1]
import csv
with open('roc_test.dat') as f:
    rd = csv.reader(f, delimiter=" ")
    for line in rd:
        a.append(float(line[0]))
        b.append(float(line[1]))

fig = plt.figure()
plt.scatter(a,b)
plt.show()
fig.savefig('roc.pdf', bbox_inches='tight')


#c = [1,2,3,4,5,6,7,8,9,10]
#d = [1,4,9,16,25,36,49,64,81,100]
#print len(a)
