class QualityDistribution(object):
    QD = {}
    def __init__(self, runID, sampleID):
        self.runID = runID
        self.sampleID = sampleID

    def addQualityBin(self, Quality, Count):
        self.QD[Quality] = Count
        return 0
    
    def toList(self):
        out = []
        for quality in self.QD:
            out.append("{0}:{1}".format(quality, self.QD[quality]))
        return out
    
    def toDatabaseEntry(self):
        out = []
        for quality in self.QD:
            out.append((self.sampleID, quality, self.QD[quality]))
        return out
        
    def getRunID(self):
        return self.runID
    
    def getSampleID(self):
        return self.sampleID