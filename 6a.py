import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 20, 10)
print(x)

y1 = x
y2 = np.square(x)
y3 = np.sqrt(x)

print(y2)
print(y3)

# Correcting the plot markers
plt.plot(x, y1, 'r', label='x')  # Line with circle markers
plt.plot(x, y2, 'g', label='y = square')  # Line with square markers
plt.plot(x, y3, 'b', label='square-root')  # Line with triangle markers

plt.legend()
plt.title("Line Plot - Nischith Gouda R - 1K23CS122")
plt.xticks(x)
plt.yticks(y2)
plt.show()