from numpy import *

class DataTable(object):
    pass

class PlateMeas(object):
    def __init__(self, pathToFile):
        self.pathToFile = pathToFile
        with open(self.pathToFile) as f:
            self.linesinfile = f.readlines()
        #array = [self.plateID(), self.MeasDate(), self.ResidRadErrRMS()]
        #print array

    def plateID(self):
        for line in self.linesinfile:
            splitLine = line.split()
            if splitLine[0] == "PlugPlate":
                    self.plateID = int(line.split()[1])
                    #print self.plateID
        # another way
        #f = open(self.pathToFile)
        #for line in f.readlines():
        #    if "PlugPlate" in line:
        #        self.plateID = int(line.split()[1])
        #        print "second", self.plateID
        #f.close()


    def MeasDate(self):
        for line in self.linesinfile:
            splitLine = line.split()
            if splitLine[0] == "MeasDate":
                self.MeasDate = str(line.split()[1])
                #print self.MeasDate

    def ResidRadErrRMS(self):
        for line in self.linesinfile:
            splitLine = line.split()
            if splitLine[0] == "ResidRadErrRMS":
                self.ResidRadErrRMS = float(line.split()[2])
                #print self.ResidRadErrRMS


plate1 = PlateMeas('/Users/tiffanyjansen/Documents/SDSSWork/examplefits.txt')
#plate1.plateID()
#plate1.MeasDate()
#plate1.ResidRadErrRMS()
