'''
Gera um gráfico de barras do preço por categoria passada como parâmetro.
'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def bar_plot(file, info):
    df = pd.read_csv(file)
    avg = df.groupby(info).mean()
    avg.plot.bar(y='SalePrice')
    plt.xlabel(info)
    plt.ylabel('Sale Price Average')
    plt.show()