import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure outputs directory exists
os.makedirs("outputs/results", exist_ok=True)

# Function to create bar plots
def plot_frequencies(observed, theoretical, dataset_name):
    x = range(1, 10)
    plt.bar(x, [observed.get(d, 0) for d in x], alpha=0.7, label="Observed")
    plt.plot(x, [theoretical[d] for d in x], marker="o", label="Theoretical", color="red")
    plt.title(f"Benford's Law: {dataset_name}")
    plt.xlabel("First Digit")
    plt.ylabel("Frequency")
    plt.legend()
    plt.savefig(f"outputs/results/{dataset_name}_comparison.png")
    plt.clf()

# Visualize results
theoretical = {d: np.log10(1 + 1 / d) for d in range(1, 10)}
results = pd.read_csv("outputs/results/benfords_results.csv")

for _, row in results.iterrows():
    dataset_name = row["dataset"].replace(".csv", "")
    data = pd.read_csv(f"outputs/datasets/{row['dataset']}")["value"]
    observed = data.astype(str).str[0].astype(int).value_counts(normalize=True).sort_index().to_dict()
    plot_frequencies(observed, theoretical, dataset_name)