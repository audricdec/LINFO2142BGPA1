import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# Data to plot
labels = 'Stub ASes', 'Non-Stub ASes'
sizes = [101026, 11464]

# Definitions
colors = ['lightcoral','gold']

# explode 1st slice
explode = (0.05, 0)

# Plot
plt.title('Proportion of stub ASes in 2022',fontsize = 16)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.legend(labels, loc="upper right")

plt.axis('equal')
plt.savefig('proportionStubASes2022.png',dpi = 100,format='png')
plt.show()