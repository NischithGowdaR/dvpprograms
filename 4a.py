import matplotlib.pyplot as plt

std = ['SSLC', 'PUC', '1st sem', '2nd sem']
marks = [95, 90, 85, 79]

plt.title("Nischith Gowda R - 1K123CS122")
plt.bar(std, marks)
plt.xlabel("Standard", fontsize=12)
plt.ylabel("Marks", fontsize=12)
plt.show()