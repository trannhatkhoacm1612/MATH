import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [2, 4, 6])

ax.tick_params(axis='x', which='major', direction='in', length=20, width=1, color='r', labelsize=20)
plt.show()