import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

def corr_matrix(data):
    df = pd.read_csv(data)
    corrMatrix = df.corr()
    corrMatrix.to_csv('corr_matrix.csv')
    sn.heatmap(corrMatrix, cmap='Greens')
    plt.show()