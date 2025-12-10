import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import treeChar as tc

def main():
    print("Tree Cruncher v1.0")
    dataset = pd.read_excel("DBHValidation_11-10-2025_11-11-2025.xlsx", sheet_name="Data (Same Num Stems)")  # Load dataset from Excel file
    print("Dataset loaded successfully.")
    row = dataset.iloc[0]  # Access the first row of the dataset
    print(row.iloc[0])











if __name__ == "__main__": #ensures that main() runs only when executed directly
    main()