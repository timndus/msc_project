# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np
import csv
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

y5 = []
y10 = []

with open('nemesis/default_nemesis_repeat_32.log','r') as csvfile:
    plots = csv.reader(csvfile, delimiter='\n')
    for row in plots:
        y5.append(float(row[0]))

with open('sock/default_sock_repeat_32.log','r') as csvfile:
    plots = csv.reader(csvfile, delimiter='\n')
    for row in plots:
        y10.append(float(row[0]))


plt.plot(y5, label='default_nemesis_repeat_32')
plt.plot(y10, label='default_sock_repeat_32')


plt.xlabel('Sample Number')
plt.ylabel('Execution Time (sec)')
ax.grid(which='both')
#plt.xticks(np.arange(0, 20, 3))
#plt.yticks(np.arange(65, 86, 5))
plt.legend()
plt.savefig('default_repeat_32.png', dpi=500)
plt.show()
