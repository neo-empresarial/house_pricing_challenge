import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def hist_plot(file, info):
    df = pd.read_csv(file)
    df.hist(info, bins=20)
    plt.xticks(np.arange(50000, 750000, step=50000))
    plt.show()