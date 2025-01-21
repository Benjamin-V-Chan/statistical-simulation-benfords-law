# statistical-simulation-benfords-law

# Benford's Law Simulation and Analysis

## Project Overview
Benford's Law is a statistical principle that predicts the frequency distribution of leading digits in many naturally occurring datasets. Unlike uniform distributions, where all digits are equally likely, Benford's Law states that smaller digits appear more frequently as the leading digit. This law is mathematically represented as:

```
P(d) = log10(1 + 1/d)
```

Where:
- `P(d)` is the probability of the digit `d` (for `d` = 1, 2, ..., 9) being the leading digit.

### Example Probabilities
- The probability of the leading digit being `1` is approximately 30.1%.
- The probability of the leading digit being `9` is about 4.6%.

### Applications
Benford's Law is widely used in:
- Fraud detection (e.g., tax records, financial statements).
- Scientific data validation.
- Assessing the authenticity of datasets.

This project simulates datasets from different distributions, analyzes their adherence to Benford's Law, and provides visualizations of the results.

---

## Folder Structure
The project is organized as follows:

```
benfords-law-simulation/
├── scripts/                    # Contains Python scripts for the simulation and analysis
│   ├── 01_generate_dataset.py  # Generates synthetic datasets
│   ├── 02_apply_benfords_law.py # Analyzes datasets and compares observed vs. theoretical distributions
│   ├── 03_visualize_results.py # Creates visualizations for results
├── outputs/                    # Stores outputs from the scripts
│   ├── datasets/               # Generated datasets
│   ├── results/                # Analysis results and visualizations
├── README.md                   # Project documentation
```

---

## Usage

### Step 1: Generate Datasets
Run the dataset generation script to create synthetic datasets:
```bash
python scripts/01_generate_dataset.py
```
This script generates datasets in the `outputs/datasets` folder, including:
- Uniform distribution
- Exponential distribution
- Lognormal distribution

### Step 2: Analyze with Benford's Law
Run the analysis script to calculate and compare observed frequencies with Benford's Law:
```bash
python scripts/02_apply_benfords_law.py
```
Results, including metrics like chi-squared statistics, will be saved in the `outputs/results` folder.

### Step 3: Visualize Results
Generate visualizations comparing observed and theoretical distributions:
```bash
python scripts/03_visualize_results.py
```
Plots will be saved in the `outputs/results` folder as `.png` files.

---

## Requirements

Before running the scripts, install the required Python packages:
```bash
pip install -r requirements.txt
```

### Dependencies
- `numpy`: For dataset generation and numerical calculations.
- `pandas`: For data manipulation and analysis.
- `matplotlib`: For creating visualizations.
- `os`: For handling file and directory operations (part of the Python standard library).

---

## Notes
This project is modular and designed for extensibility. You can:
1. Add new dataset types in `01_generate_dataset.py`.
2. Implement alternative statistical tests in `02_apply_benfords_law.py`.
3. Customize or expand visualizations in `03_visualize_results.py`.

Feel free to explore, modify, and enhance the project to meet your needs!