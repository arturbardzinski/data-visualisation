import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squeres = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squeres, linewidth=3)

ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()