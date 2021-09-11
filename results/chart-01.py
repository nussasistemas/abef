import matplotlib.pyplot as plt
import matplotlib.path as mpath
import numpy as np


star = mpath.Path.unit_regular_star(6)
circle = mpath.Path.unit_circle()
# concatenate the circle with an internal cutout of the star
verts = np.concatenate([star.vertices, star.vertices[::-1, ...]])
codes = np.concatenate([star.codes, star.codes])
cut_star = mpath.Path(verts, codes)

# Using readlines()
file1 = open('_results_abef_01.csv', 'r')
Lines = file1.readlines()

data = []
y_axis = []
i = 1
for line in Lines:
    data.append(line.split(', ')[1])
    y_axis.append(i)
    i += 1

# plt.plot(y_axis, data, '--b', marker=cut_star, markersize=5)
# # plt.savefig('chart-01.svg')
# plt.show()

t = y_axis
s = data
plt.plot(s)

plt.ylim(0, 1)  # decreasing time
plt.xlim(min(y_axis), 40)  # decreasing time

plt.xlabel('decreasing time (s)')
plt.ylabel('voltage (mV)')
plt.title('Should be growing...')
plt.grid(True)

plt.show()
