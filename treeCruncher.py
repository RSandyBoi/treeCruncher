
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import treeChar as tc
from scipy.stats import zscore
import os


# #TODO Placeholder functions for getting trees from different cities/municipalities, await new data from Katherine 

#usage:
#dataset: the dataset to be filtered for the desired city/municipality, should be a sorted (ideal) numpy array of Tree objects 
#return: a sorted numpy array of Tree objects that match the desired city/municipality
def get_federal_way_trees(dataset): # Function to get Federal Way trees
    pass  # Placeholder for the actual implementation
def get_milton_trees(dataset): # Function to get Milton trees
    pass  # Placeholder for the actual implementation
def get_Tacoma_trees(dataset): # Function to get Tacoma trees
    pass  # Placeholder for the actual implementation  
def get_puyallup_trees(dataset): # Function to get Puyallup trees
    pass  # Placeholder for the actual implementation
def get_WSDOT_trees(dataset): # Function to get WSDOT trees
    pass  # Placeholder for the actual implementation
def get_Pierce_County_trees(dataset): # Function to get Pierce County trees
    pass  # Placeholder for the actual implementation


##TODO Plotter function to create and display a plot for the given dataset and labels, modularized for reusability and for creating multiple independent figures. Improve for stylistic choices
#Usage: 
#plot_id: unique identifier for the plot, used to create a new figure for each plot
#dataset: the dataset to be plotted, which should be a list of lists, where each inner list contains the data for a specific bucket
#labels: the labels for the x-axis, which should be a list of strings
#title: the title of the plot, which should be a string
#x_label: the label for the x-axis, which should be a string
#y_label: the label for the y-axis, which should be a string
def  scatter_plotter(plot_id, dataset, labels, title, x_label, y_label): 
    plt.figure(plot_id, figsize=(20, 8))  # Create a figure with a specified size
    for y_data, label in zip(dataset, labels):  # Iterate through each bucket's dbh deltas and labels
        for i in y_data:  # Iterate through each delta in the current bucket
            plt.scatter(label, i, s=20, color = 'blue')  # Plot each delta as a scatter point with the corresponding label
        plt.errorbar(label, np.mean(y_data), yerr=np.std(y_data), fmt='o', color='red', ecolor='red', capsize=5, elinewidth=2)  # Add error bars to the plot
    plt.title(title)  # Set the title of the plot
    plt.xlabel(x_label)  # Set the label for the x-axis
    plt.ylabel(y_label)  # Set the label for the y-axis
    plt.grid(True)  # Add a grid to the plot for better readability


    
def data_filler(filepaths): # Implement the data filler function to load and process data from the provided file paths, returns a Numpy array of Tree objects
    trees = np.array([], dtype=object)  # Initialize an empty numpy array to hold Tree objects
    for filepath in filepaths:  # Iterate through each file path in the list of file paths
        print(f"Loading data from {filepath}...")  # Print a message indicating the file being loaded
        data = pd.read_csv(filepath, encoding='cp1252')  # Read the CSV file into a pandas DataFrame, encoding set to cp1252 to handle special characters
        for index, row in data.iterrows():  # Iterate through each row in the DataFrame
            if pd.isna(row.iloc[0]):  # Data quality check to ensure pure numeric IDs using ID column to indicate end of readable data
                continue
            tree = tc.Tree(
                ID=row['ID'],
                DBH1=row['DBH (II)'],
                DBH2=row['DBH (DV)'],
                stemsInitial=row['Num Stems (II)'],
                stemsValidated=row['Num Stems (DV)']
            )  # Create a Tree object for the current row
            trees = np.append(trees, tree)  # Append the Tree object to the numpy array
    return trees  



def main():
    print("Tree Cruncher v0.5")

    target_folder = "./DBH data CSV's"  # target directory for the datasets to be used <----------------------CHANGE PER DIRECTORY CHANGES
    filenames = os.listdir(target_folder)  # List all files in the target directory
    print("Files in target folder:", filenames)  # Print the list of files in the target directory
    file_paths = []  # List to hold the full paths of the files
    for filename in filenames:  # Iterate through each file in the target directory
        full_path = os.path.join(target_folder, filename)  # Get the full path of the file
        file_paths.append(full_path)  # Add the full path to the list of file paths

    #* Create Tree objects from dataset *#
    trees = data_filler(file_paths)  

    
        
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

####^^#TODO Modularize the above bucketing process into a function to be called with different datasets and bucketing criteria, as needed for different cities/municipalities. include documentation for each 

    print("total tree credits: ", len(tree_credit_1) + len(tree_credit_1_5)*1.5 + len(tree_credit_2)*2 + len(tree_credit_2_5)*2.5 + len(tree_credit_3)*3) # Calculate and print the total tree credits based on the number of trees in each bucket and their respective credit values.
    dbh_delta_values_1 = [tree.delta for tree in tree_credit_1]  # Extract delta values from bucket 1
    dbh_delta_values_1_5 = [tree.delta for tree in tree_credit_1_5]  # Extract delta values from bucket 1.5
    dbh_delta_values_2 = [tree.delta for tree in tree_credit_2]
    dbh_delta_values_2_5 = [tree.delta for tree in tree_credit_2_5]
    dbh_delta_values_3 = [tree.delta for tree in tree_credit_3]

    dbh_deltas = [dbh_delta_values_1, dbh_delta_values_1_5, dbh_delta_values_2, dbh_delta_values_2_5, dbh_delta_values_3]  # Combine delta values from all buckets into a single list
    dbh_delta_column_labels = ['bucket 1', 'bucket 1.5', 'bucket 2', 'bucket 2.5', 'bucket 3']  # Create a list of labels for the delta values in each bucket
    z_scores = [zscore(bucket) for bucket in dbh_deltas]  # Calculate the z-scores for the delta values in each bucket
     
    ##^Keep above for debugging purposes, but comment out for final version to keep the output clean and focused on the plots. good for reminders of how to utilize numpy functions for statistical analysis.

    # Plotting the delta dbh values for each bucket
    scatter_plotter(1, dbh_deltas, dbh_delta_column_labels, "Delta DBH Values by Tree Credit Bracket", "Tree Credit Bracket", "Delta DBH (inches)")  # Call the plotter function to create and display the plot for delta DBH values by tree credit bracket
    scatter_plotter(2, z_scores, dbh_delta_column_labels, "Z-Scores of Delta DBH Values by Tree Credit Bracket", "Tree Credit Bracket", "Z-Score")  # Call the plotter function to create and display the plot for z-scores of delta DBH values by tree credit bracket

    plt.show()  # Display the figure with all subplots










if __name__ == "__main__": #ensures that main() runs only when executed directly
    main()