import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(15,-15,100) # 100 linearly spaced numbers

# red dashes, blue squares and green triangles
plt.plot((x**3)/((np.exp(x)-1)))
plt.show()
