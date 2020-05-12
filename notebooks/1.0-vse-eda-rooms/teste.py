import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def line_plt(file):
    df = pd.read_csv(file)
    cont = df.GarageYrBlt.value_counts()
    cont.plot.line()
    plt.show()