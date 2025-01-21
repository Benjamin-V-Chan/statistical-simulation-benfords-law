import pandas as pd
import numpy as np
import os

# Ensure outputs directory exists
os.makedirs("outputs/results", exist_ok=True)

# Function to calculate first-digit frequencies
def calculate_first_digit_frequencies(data):
    first_digits = data.astype(str).str[0].astype(int)
    frequencies = first_digits.value_counts(normalize=True).sort_index()
    return frequencies

# Function to calculate Benford's Law theoretical frequencies
def benfords_law_frequencies():
    return {d: np.log10(1 + 1 / d) for d in range(1, 10)}

# Compare datasets to Benford's Law
results = []
datasets = [f for f in os.listdir("outputs/datasets") if f.endswith(".csv")]
theoretical = benfords_law_frequencies()

for dataset in datasets:
    data = pd.read_csv(f"outputs/datasets/{dataset}")["value"]
    observed = calculate_first_digit_frequencies(data)
    observed_dict = observed.to_dict()
    chi_squared = sum((observed_dict.get(d, 0) - theoretical[d])**2 / theoretical[d] for d in range(1, 10))
    results.append({"dataset": dataset, "chi_squared": chi_squared})

# Save results
results_df = pd.DataFrame(results)
results_df.to_csv("outputs/results/benfords_results.csv", index=False)