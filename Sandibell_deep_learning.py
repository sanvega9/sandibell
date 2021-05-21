import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

Ice_cream = pd.read_csv("TemplCSalesData - Sheet1.csv")

graph = pd.DataFrame(np.random.rand(10,2),columns=["Temp", "Cones Sold"])
graph.plot.box()
plt.show()

sns.barplot(x=Ice_cream['Temp'],y=Ice_cream['Cones Sold'])

plt.show()

sns.lineplot(data=Ice_cream,x="Temp",y="Cones Sold")
plt.show()