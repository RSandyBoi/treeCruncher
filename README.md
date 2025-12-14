This program is designed to take in Tree data from a tree inventory dataset and utilize it for statistical analysis. Comes with Pyplot functionality

Made by Ryan Sanderson, for purposes related to Atlas Technical Consultants, Environmental Division.

Made for use with Tacoma Dome Link Extension Data, provided by Katherine Feldmann, collected in the field by Atlas Arborist Staff

IMPORTANT:
Files utilized must be placed in folder within the working directory called "DBH data CSV's", and must be uploaded as CSV's. CSV data must also conform to a standard before being processed, namely it must have the following column headers (Without the {}): {ID}, {DBH (II)}, {DBH (DV)}, {Num Stems(II)}, {Num Stems (DV)}. Additionally, the only string (text) value allowed is the ID column, all other columns must be Integers or Floats.

Failure to do so **Will** result in an error. You have been warned.

#TODO Jurisdictions of interest are:
-Federal Way (implemented as base case)
-Tacoma
-Milton
-Puyallup
-WSDOT
-Pierce County
