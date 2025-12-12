
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import treeChar as tc

def main():
    print("Tree Cruncher v1.0")

    #* Load dataset *#
    dataset = pd.read_excel("DBHValidation_11-10-2025_11-11-2025.xlsx")  # Load dataset from Excel file
    print("Dataset loaded successfully.")
    
    
    #* Create Tree objects from dataset *#
    trees = np.array([], dtype=object)  # List to hold Tree objects
    
    # Iterate through each row in the dataset, create a Tree object for each valid row, and append it to the trees array
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
        # values currently hard coded based on known dataset structure, may need to be adjusted for different datasets. Consider csv input option in future to use header names instead
        
        trees = np.append(trees, tree)
        
    print(f"Total Trees Created: {len(trees)}, ready for analysis.")

    #sort trees by dbh2 from tree objects
    sorted_trees = sorted(trees, key=lambda tree: tree.DBH2)  # Sort trees by DBH2 in ascending order
    sorted_trees = np.array(sorted_trees, dtype=object)  # Convert sorted list back to numpy array
    print("Trees sorted by DBH2.")

    #bucketing trees by dbh2
    buckets = np.array([], dtype=object)  # List to hold buckets of trees
    # Create buckets of trees based on DBH2 values, with each bucket containing trees with DBH2 values within a specific range#

    for tree in sorted_trees:
        if tree.DBH2 < 10:
            bucket = np.array([], dtype=object)
            bucket = np.append(bucket, tree)
            buckets = np.append(buckets, bucket)
        elif 10 <= tree.DBH2 < 20:
            bucket = np.array([], dtype=object)
            bucket = np.append(bucket, tree)
            buckets = np.append(buckets, bucket)
        elif 20 <= tree.DBH2 < 30:
            bucket = np.array([], dtype=object)
            bucket = np.append(bucket, tree)
            buckets = np.append(buckets, bucket)
        elif 30 <= tree.DBH2 < 40:
            bucket = np.array([], dtype=object)
            bucket = np.append(bucket, tree)
            buckets = np.append(buckets, bucket)
        elif 40 <= tree.DBH2 < 50:
            bucket = np.array([], dtype=object)
            bucket = np.append(bucket, tree)
            buckets = np.append(buckets, bucket)
        elif 50 <= tree.DBH2 < 60:
            bucket = np.array([], dtype=object)
            bucket = np.append(bucket, tree)
            buckets = np.append(buckets, bucket)
        elif 60 <= tree.DBH2 < 70:
            bucket = np.array([], dtype=object)
            bucket = np.append(bucket, tree)
            buckets = np.append(buckets, bucket)
        elif 70 <= tree.DBH2 < 80:
            bucket = np.array([], dtype=object)
            bucket = np.append(bucket, tree)
            buckets = np.append(buckets, bucket)
        elif 80 <= tree.DBH2 < 90:
            bucket = np.array([], dtype=object)
            bucket = np.append(bucket, tree)
            buckets = np.append(buckets, bucket)
        elif 90 <= tree.DBH2 < 100:
            bucket = np.array([], dtype=object)
            bucket = np.append(bucket, tree)
            buckets = np.append(buckets, bucket)
        else:
            bucket = np.array([], dtype=object)
            bucket = np.append(bucket, tree)
            buckets = np.append(buckets, bucket)
    
    """    
    #row = dataset.iloc[0]  # Access the first row of the dataset
    #print(row.iloc[0]) # prints the first element of the first row
    #EXAMPLE OF HOW TO ACCESS DATA IN THE DATASET
    """











if __name__ == "__main__": #ensures that main() runs only when executed directly
    main()