import matplotlib.pyplot as plt
import numpy as np

class Tree:
    def __init__(self, ID, species_code, height, DBH1, DBH2, health_status):
        self.ID = ID
        self.species_code = species_code
        self.height = height
        self.DBH1 = DBH1
        self.DBH2 = DBH2
        self.health_status = health_status
        self.delta = abs(DBH1 - DBH2)

    def get_id(self):
        return self.ID
    def get_species_code(self):
        return self.species_code
    def get_height(self):
        return self.height
    def get_DBH1(self):
        return self.DBH1
    def get_DBH2(self):
        return self.DBH2
    def get_delta(self):
        return self.delta
    def get_health_status(self):
        return self.health_status

    def plot(self):
        plt.hist(self.data, bins=30, alpha=0.7, color='blue')
        plt.axvline(self.mean, color='red', linestyle='dashed', linewidth=1)
        plt.title('Data Distribution')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.show()