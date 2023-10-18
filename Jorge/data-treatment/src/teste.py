import matplotlib.pyplot as plt
import pandas as pd

normalized = pd.read_csv('../datasheets/normalized.csv')

colors = {"hand_open":"orange", "hand_flex_curl":"blue"}

for i in range(0,4):
    plt.plot(range(len(normalized[f"ch{i}"])), normalized[f"ch{i}"])
    plt.title(f"normalized filtered signal colored by gesture channel {i}")
    plt.show()