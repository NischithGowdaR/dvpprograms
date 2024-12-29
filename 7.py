import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def sineplot(n=10):
    x = np.linspace(0, 15, 20)

    for i in range(1, n+1):
        plt.plot(x, np.sin(x + i * 0.5) * (n+2-i))
sns.set_context("talk")
sineplot()
plt.title("Nischith Gowda R - 1K23CS122")
plt.show()