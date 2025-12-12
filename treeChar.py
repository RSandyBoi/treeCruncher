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
        self.delta = self.DBH2-self.DBH1 # Calculate the difference between DBH1 and DBH2