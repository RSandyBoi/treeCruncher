
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import treeChar as tc

def main():
    print("Tree Cruncher v1.0")
    dataset = pd.read_excel("DBHValidation_11-10-2025_11-11-2025.xlsx")  # Load dataset from Excel file
    print("Dataset loaded successfully.")
    
    
    #* Create Tree objects from dataset *#
    trees = np.array([], dtype=object)  # List to hold Tree objects
    
    for index, row in dataset.iterrows():
        if pd.isna(row.iloc[0]): #data QC to ensure pure numeric IDs using ID column to indicate end of readable data
            print("Invalid Tree ID encountered, skipping this entry.")
            continue
        tree = tc.Tree(
            ID=row.iloc[0],
            species_code=row.iloc[2],
            DBH1=row.iloc[6],
            DBH2=row.iloc[7]
        )
        
        trees = np.append(trees, tree)
        
    print(f"Total Trees Created: {len(trees)}")
    print(trees[0].get_id())  # Example: Print ID of the first tree
        
    ############################    
    #row = dataset.iloc[0]  # Access the first row of the dataset
    #print(row.iloc[0]) # prints the first element of the first row
    #EXAMPLE OF HOW TO ACCESS DATA IN THE DATASET
    ############################











if __name__ == "__main__": #ensures that main() runs only when executed directly
    main()