# statistical-simulation-benfords-law

## Project Overview
This project investigates **Benford's Law**, a statistical principle describing the distribution of leading digits in numerical data. According to Benford's Law, the leading digit of many naturally occurring datasets is more likely to be smaller numbers (e.g., 1, 2) than larger ones (e.g., 8, 9). The probability of a number's leading digit being `d` is calculated using the formula:

```
P(d) = log10(1 + 1/d)
```

Where:
- `P(d)` is the probability of the leading digit `d` (for `d` = 1, 2, ..., 9).

Key probabilities include:
- Leading digit `1`: ~30.1% chance.
- Leading digit `9`: ~4.6% chance.

### Applications of Benford's Law
- Fraud detection in accounting and financial records.
- Validation of datasets in scientific research.
- Analysis of naturally occurring numbers such as populations, stock prices, and physical constants.

This project simulates datasets, applies Benford's Law, and visualizes the results to illustrate how well different datasets conform to the expected distribution.

---

## Folder Structure
The project is organized as follows:

```
project-root/
├── scripts/                     # Python scripts for simulation and analysis
│   ├── 01_generate_dataset.py   # Generates synthetic datasets
│   ├── 02_apply_benfords_law.py # Analyzes datasets and compares distributions
│   ├── 03_visualize_results.py  # Creates visualizations of results
├── outputs/                     # Stores output files
│   ├── datasets/                # Generated datasets
│   ├── results/                 # Analysis results and visualizations
├── requirements.txt             # Required Python packages
├── README.md                    # Project documentation
```

---

## Usage

### Step 1: Setup the Project
1. Clone the repository.
2. Ensure you have Python installed.
3. Install required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Step 2: Generate Datasets
Run the dataset generation script to create synthetic datasets:

```bash
python scripts/01_generate_dataset.py
```

This will generate datasets based on various distributions (e.g., uniform, exponential, and lognormal) and save them in the `outputs/datasets` folder.

### Step 3: Analyze Datasets with Benford's Law
Run the analysis script to compare the observed leading-digit frequencies with the theoretical distribution:

```bash
python scripts/02_apply_benfords_law.py
```

The script calculates metrics such as chi-squared statistics and saves the results as a CSV in the `outputs/results` folder.

### Step 4: Visualize Results
Generate visualizations comparing observed and theoretical distributions by running the visualization script:

```bash
python scripts/03_visualize_results.py
```

The visualizations will be saved in the `outputs/results` folder as `.png` files.

---

## Requirements
To run the project, you need the following Python packages:
- `numpy`: For generating synthetic data and performing numerical calculations.
- `pandas`: For handling and analyzing datasets.
- `matplotlib`: For creating visualizations.

To install the required packages, run:

```bash
pip install -r requirements.txt
```
