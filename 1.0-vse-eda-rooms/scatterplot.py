'''
Gera um gráfico de dispersão dos dados passados como parâmetro.
'''

import pandas as pd
import matplotlib.pyplot as plt

def scatter_plot(file, info):

    df = pd.read_csv(file)
    df.plot.scatter(x=info, y='SalePrice')
    plt.show()