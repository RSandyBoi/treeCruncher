import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Tree:
    def __init__(self, ID, species_code, height, DBH, health_status):
        self.ID = ID
        self.species_code = species_code
        self.height = height
        self.DBH = DBH
        self.health_status = health_status

    def plot(self):
        plt.hist(self.data, bins=30, alpha=0.7, color='blue')
        plt.axvline(self.mean, color='red', linestyle='dashed', linewidth=1)
        plt.title('Data Distribution')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.show()