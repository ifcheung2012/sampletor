__author__ = 'ifcheung'
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

F = np.arange(-50, 240, 0.1)
C = (F - 32)/1.8

# Basic
plt.plot(F, C, 'r-', linewidth = 0.5)
plt.title('Convert the unit of temperature')

# Revise, ticks
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(2))
ax.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(2))
plt.grid(b = True)

sc = np.array([-40, -20, 0, 20, 37, 60, 80, 100])
sf = np.array([-40, 0, 32, 80, 37*1.8+32, 140, 180, 100*1.8+32])
plt.yticks(sc); plt.xticks(sf)

# Label the specific temperatures
plt.scatter([32, ], [0, ], 50, color = 'blue')
plt.plot([0, 37*1.8+32], [37, 37], color = 'blue', linewidth = 2.5, linestyle = '--')
plt.plot([37*1.8+32, 37*1.8+32], [0, 37], color = 'blue', linewidth = 2.5, linestyle = '--')
plt.scatter([37*1.8+32, ], [37, ], 50, color = 'blue')
plt.plot([0, 100*1.8+32], [100, 100], color = 'blue', linewidth = 2.5, linestyle = '--')
plt.plot([100*1.8+32, 100*1.8+32], [0, 100], color = 'blue', linewidth = 2.5, linestyle = '--')
plt.scatter([100*1.8+32, ], [100, ], 50, color = 'blue')

plt.xlabel('Fahrenheit')
plt.ylabel('Centigrade')

plt.savefig('FtoC1.png')
plt.close()