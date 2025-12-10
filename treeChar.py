class Tree:
    def __init__(self, ID, species_code, DBH1, DBH2):
        #self.tag = tag #tag is not used in the current dataset, await further info
        #Initialize tree attributes
        #self.health_status = health_status #health_status is not used in the current dataset, await further info
        #self.height = height
        self.ID = ID
        self.species_code = species_code
        self.DBH1 = float(DBH1)
        self.DBH2 = float(DBH2)
        self.delta = self.DBH1 - self.DBH2 # Calculate the difference between DBH1 and DBH2
    # Getter methods for each attribute
    def get_id(self):
        return self.ID
    def get_species_code(self):
        return self.species_code
    #def get_height(self):
    #    return self.height
    def get_DBH1(self):
        return self.DBH1
    def get_DBH2(self):
        return self.DBH2
    def get_ABSdelta(self):
        return abs(self.delta)
    def get_delta(self):
        return self.delta
    #def get_health_status(self):
    #    return self.health_status