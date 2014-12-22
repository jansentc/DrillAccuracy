from numpy import *
import glob

class PlateMeas(object):
    def __init__(self, pathToFile):
        self.pathToFile = pathToFile
        with open(self.pathToFile) as f:
            self.linesinfile = f.readlines() 
        #array = [self.plateID(), self.MeasDate(), self.ResidRadErrRMS()]  #Before, when I was trying to create the array [self.plateID,...] 
        #print array                             #I was just giving it the function
                                                #name, not telling it to DO the function. We fix this by doing self.plateID(), 
                                                #which will return whatever that function returns.            
            
    def plateID(self):
        for line in self.linesinfile:
            splitLine = line.split()
            if splitLine[0] == "PlugPlate":
                    return int(line.split()[1]) 
                    
        # another way 
        #f = open(self.pathToFile)
        #for line in f.readlines():
        #    if "PlugPlate" in line:
        #        self.plateID = int(line.split()[1])
        #        print "second", self.plateID
        #f.close()
            
            
    def measDate(self):
        for line in self.linesinfile:
            splitLine = line.split()
            if splitLine[0] == "MeasDate":
                return str(line.split()[1])
                #print self.MeasDate
    
    def residRadErrRMS(self):
        for line in self.linesinfile:
            splitLine = line.split()
            if splitLine[0] == "ResidRadErrRMS":
                return float(line.split()[2])
                #print self.ResidRadErrRMS
                
    def createArray(self):
        return [self.plateID(), self.measDate(), self.residRadErrRMS()] 
                
    
            
#testplate = PlateMeas('/Users/tiffanyjansen/Documents/SDSSWork/examplefits.txt')
#test = testplate.createArray()
#print test

stringfilenames = '/Users/tiffanyjansen/GitHub/DrillAccuracy/tests/testData/fit*.txt'
filenameList = glob.glob(stringfilenames)
#print filenameList

codeOutput = open('codeOutput.txt', 'w')
#outarray = []
for filename in filenameList:
    pm = PlateMeas(filename).createArray()
    outarray = array(pm) 
    #print outarray
    codeOutput.write(str(outarray) + '\n')
codeOutput.close()

PlateID, MeasDate, ResidRadErrRMS = loadtxt('codeOutput.txt', dtype = 'string', usecols = (0,1,2), unpack = True)


