import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

colors = {"hand_open":"orange", "hand_flex_curl":"blue"}

def rolling_mean(window, datasheet, channels=4):
    result = datasheet.copy()
    for i in range(channels):
        result[f"ch{i}"] = np.rolling(window).mean(result[f"ch{i}"])
    return result

def rolling_median(window, datasheet, channels=4):
    result = datasheet.copy()
    for i in range(channels):
        result[f"ch{i}"] = np.rolling(window).median(result[f"ch{i}"])
    return result

def normalize_datasheet(datasheet, channels=4):
    result = datasheet.copy()
    for i in range(channels):
        max_value = np.max(result[f"ch{i}"])
        min_value = np.min(result[f"ch{i}"])
        result[f"ch{i}"] = 2 * (result[f"ch{i}"] - min_value) / (max_value - min_value)
    return result

def maximum_filter(datasheet, window, channels=4):
    result = datasheet.copy()
    for i in range(channels):
        result[f"ch{i}"] = ndimage.maximum_filter(result[f"ch{i}"], size=window)
    return result

def center_datasheet(datasheet, window, channels=4):
    result = datasheet.copy()
    for i in range(channels):
        result[f"ch{i}"] = result[f"ch{i}"] - np.rolling(window).mean(result[f"ch{i}"])
    return result

def generate_graphs(datasheet, ranges=None, channels=4):
    if (ranges == None):
        for i in range(channels):
            plt.figure(figsize=(20,6))
            plt.scatter(range(len(datasheet[f"ch{i}"])), datasheet[f"ch{i}"], color=datasheet["gesture"].map(colors), s=1)
            plt.title(f"Channel {i}")
            plt.show()
        return
        
    for i in range(channels):
        plt.figure(figsize=(20,6))
        plt.scatter(range(len(datasheet[f"ch{i}"][:ranges])), datasheet[f"ch{i}"][:ranges], color=datasheet["gesture"][:ranges].map(colors), s=1)
        plt.title(f"Channel {i} in range(0, {ranges})")
        plt.show()
