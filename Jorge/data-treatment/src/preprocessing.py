import pandas as pd
from operations import rolling_mean, rolling_median, normalize_datasheet, center_datasheet, generate_graphs

datasheet = pd.read_csv("../datasheets/original.csv", delimiter=";")

median = rolling_median(9, datasheet)
mean = rolling_mean(100, median)
normalized = normalize_datasheet(mean)
centered = center_datasheet(100, normalized)

generate_graphs(datasheet)
generate_graphs(median)
generate_graphs(mean)
generate_graphs(normalized)
generate_graphs(centered)