import numpy as np
import pandas as pd
import os

# Ensure outputs directory exists
os.makedirs("outputs/datasets", exist_ok=True)

# Function to generate datasets
def generate_dataset(num_samples, distribution_type):
    if distribution_type == "uniform":
        data = np.random.uniform(1, 1000, num_samples)
    elif distribution_type == "exponential":
        data = np.random.exponential(scale=50, size=num_samples)
    elif distribution_type == "lognormal":
        data = np.random.lognormal(mean=3, sigma=1, size=num_samples)
    else:
        raise ValueError("Unsupported distribution type")
    return data

# Generate and save datasets
for dist in ["uniform", "exponential", "lognormal"]:
    data = generate_dataset(10000, dist)
    df = pd.DataFrame(data, columns=["value"])
    df.to_csv(f"outputs/datasets/{dist}_dataset.csv", index=False)