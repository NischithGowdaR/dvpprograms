import matplotlib.pyplot as plt

overs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
runs_scored = [0, 7, 12, 20, 30, 40, 61, 83, 75, 97, 113, 116, 123, 130, 135, 139, 140, 145, 150, 160]

plt.plot(overs, runs_scored, marker='x', linestyle='dashed', color='blue',linewidth="2", markerfacecolor='blue', markersize=8)
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.title("Nischith Gowda R - 1K23CS122")
plt.grid(True)
plt.show()