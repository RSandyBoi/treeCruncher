class Tree:
    def __init__(self, ID, DBH1, DBH2, stemsInitial, stemsValidated):
        #Initialize tree attributes
        #self.tag = tag #tag is not used in the current dataset, await further info
        #self.health_status = health_status #health_status is not used in the current dataset, await further info
        #self.height = height #height is not used in the current dataset, await further info
        #self.species = species #species of the tree,#TODO need to debug, somehow "POBA" is recognized as an unexpected token. Very weird
        self.ID = ID
        self.DBH1 = float(DBH1)
        self.DBH2 = float(DBH2)
        self.delta = abs(self.DBH2-self.DBH1) # Calculate the difference between DBH1 and DBH2
        self.numStemsInitial = stemsInitial #number of stems
        self.numStemsValidated = stemsValidated #number of stems after validation
        self.isSame = self.numStemsInitial == self.numStemsValidated # Check if the number of stems is the same before and after validation

        #self.date_initial = date_initial #initial inventory date, is not used in the current dataset, await further info
        #self.date_validated = date_validated #validated inventory date where tree DBH was checked, is not used in the current dataset, await further info
        #self.municipality = municipality #indicates the municipality that the tree shall be subject to, is not used in the current dataset, await further info