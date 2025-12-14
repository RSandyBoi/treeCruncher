
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import treeChar as tc
from scipy.stats import zscore

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
    tree_credit_1 = np.array([], dtype=object)  # Initialize an empty bucket for 1 tree credit
    tree_credit_1_5 = np.array([], dtype=object)  # Initialize an empty bucket for 1.5 tree credits
    tree_credit_2 = np.array([], dtype=object)  # Initialize an empty bucket for 2 tree credits
    tree_credit_2_5 = np.array([], dtype=object)  # Initialize an empty bucket for 2.5 tree credits
    tree_credit_3 = np.array([], dtype=object)  # Initialize an empty bucket for 3 tree credits



    for tree in sorted_trees: # Iterate through each tree in the sorted array to organize into buckets based on DBH2 values, defined by the Federal Way "Tree and Vegetation Retention Requirements" document.
        if tree.DBH2 <= 6: #1 tree credit
            tree_credit_1 = np.append(tree_credit_1, tree)
        elif 6 < tree.DBH2 <= 12: #1.5 tree credits
            tree_credit_1_5 = np.append(tree_credit_1_5, tree)
        elif 12 < tree.DBH2 <= 18: #2 tree credits
            tree_credit_2 = np.append(tree_credit_2, tree)
        elif 18 < tree.DBH2 <= 24: #2.5 tree credits
            tree_credit_2_5 = np.append(tree_credit_2_5, tree)
        elif 24 < tree.DBH2: #3 tree credits
            tree_credit_3 = np.append(tree_credit_3, tree)
#buckets with size ranges 0-6, 6-12, 12-18, 18-24, 24+ are created and populated with trees based on their DBH2 values, per Federal Way "Tree and Vegetation Retention Requirements" document. 
# found here: https://www.federalwaywa.gov/sites/default/files/Documents/Department/CD/Planning/Land%20Use%20Apps%20and%20Info%20Handouts/069%20Tree%20and%20Vegetation%20Retention%20Requirements.pdf

    print("total tree credits: ", len(tree_credit_1) + len(tree_credit_1_5)*1.5 + len(tree_credit_2)*2 + len(tree_credit_2_5)*2.5 + len(tree_credit_3)*3) # Calculate and print the total tree credits based on the number of trees in each bucket and their respective credit values.
    dbh_delta_values_1 = [tree.delta for tree in tree_credit_1]  # Extract delta values from bucket 1
    dbh_delta_values_1_5 = [tree.delta for tree in tree_credit_1_5]  # Extract delta values from bucket 1.5
    dbh_delta_values_2 = [tree.delta for tree in tree_credit_2]
    dbh_delta_values_2_5 = [tree.delta for tree in tree_credit_2_5]
    dbh_delta_values_3 = [tree.delta for tree in tree_credit_3]

    dbh_deltas = [dbh_delta_values_1, dbh_delta_values_1_5, dbh_delta_values_2, dbh_delta_values_2_5, dbh_delta_values_3]  # Combine delta values from all buckets into a single list
    dbh_delta_column_labels = ['bucket 1', 'bucket 1.5', 'bucket 2', 'bucket 2.5', 'bucket 3']  # Create a list of labels for the delta values in each bucket
    print(f"Average delta for tree credit bracket 1: {np.average(dbh_delta_values_1)}, with bucket size {len(tree_credit_1)} trees, standard deviation of {np.std(dbh_delta_values_1)}")  
    print(f"Average delta for tree credit bracket 1.5: {np.average(dbh_delta_values_1_5)}, with bucket size {len(tree_credit_1_5)} trees, standard deviation of {np.std(dbh_delta_values_1_5)}")  
    print(f"Average delta for tree credit bracket 2: {np.average(dbh_delta_values_2)}, with bucket size {len(tree_credit_2)} trees, standard deviation of {np.std(dbh_delta_values_2)}")  
    print(f"Average delta for tree credit bracket 2.5: {np.average(dbh_delta_values_2_5)}, with bucket size {len(tree_credit_2_5)} trees, standard deviation of {np.std(dbh_delta_values_2_5)}")  
    print(f"Average delta for tree credit bracket 3: {np.average(dbh_delta_values_3)}, with bucket size {len(tree_credit_3)} trees, standard deviation of {np.std(dbh_delta_values_3)}") 

    print("Z-score calculation for delta values")
    z_scores = [zscore(bucket) for bucket in dbh_deltas]  # Calculate the z-scores for the delta values in each bucket
     
    
    # Plotting the z-score values for each bucket
    plt.figure(figsize=(20, 8))  # Create a figure with a specified size

    for y_data, label in zip(z_scores, dbh_delta_column_labels):  # Iterate through each bucket's z-scores and labels
        plt.scatter(z_scores, y_data, label=label)  # Plot the z-scores for the current bucket with the corresponding label  #    plt.xlabel('Tree Index')  # Set the label for the x-axis
    plt.show()  # Display the figure with all subplots











if __name__ == "__main__": #ensures that main() runs only when executed directly
    main()