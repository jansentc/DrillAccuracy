from numpy import *

class PlateMeas(object):
    def __init__(self, pathToFile):
        self.pathToFile = pathToFile
        with open(self.pathToFile) as f:
            self.linesinfile = f.readlines() 
        #array = [self.plateID(), self.MeasDate(), self.ResidRadErrRMS()]  
        #print array      
        #    
    def plateID(self):
        for line in self.linesinfile:
            splitLine = line.split()
            if splitLine[0] == "PlugPlate":
                    return int(line.split()[1])
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
                return str(line.split()[1])
                #print self.MeasDate
    
    def ResidRadErrRMS(self):
        for line in self.linesinfile:
            splitLine = line.split()
            if splitLine[0] == "ResidRadErrRMS":
                return float(line.split()[2])
                #print self.ResidRadErrRMS
                
    def createarray(self):
        return [self.plateID(), self.MeasDate(), self.ResidRadErrRMS()]
                    
                
    
            
plate1 = PlateMeas('/Users/tiffanyjansen/Documents/SDSSWork/examplefits.txt')
plateID = plate1.plateID()
#MeasDate = plate1.MeasDate()
#ResidRadErrRMS = plate1.ResidRadErrRMS()
print plate1.createarray()

#to create a list of textfiles, use Glob: look up Glob
#works like: globMeString = "/home/csayres/*.txt)"
#filenameList = glob.glob(globMeString)
#
#outarray = []
#for filename in filenameList:
#    pm = PlateMeas(filename)
#    outArray.append(pm.createArray)
