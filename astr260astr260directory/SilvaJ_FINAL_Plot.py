import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,25) # 100 linearly spaced numbers

plt.plot(((x**3))/((np.exp(x)-1)))
plt.show()
