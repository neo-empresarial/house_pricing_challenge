import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def line_plot(file, info):
    df = pd.read_csv(file)
    avg = df.groupby(info).mean()
    avg.plot.line(y='SalePrice')
    plt.title('Sale Price Average')
    plt.show()