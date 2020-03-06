#! /usr/bin/env python2.7
# pylint: disable=relative-beyond-top-level

from .DatabaseType import DatabaseType

class QualityDistribution(DatabaseType):
    QD = {}
    def __init__(self, runID, sampleID):
        self.runID = str(runID)
        self.sampleID = str(sampleID)

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
            out.append((str(self.sampleID), str(quality), str(self.QD[quality])))
        return out
        
    def getRunID(self):
        return self.runID
    
    def getSampleID(self):
        return self.sampleID
