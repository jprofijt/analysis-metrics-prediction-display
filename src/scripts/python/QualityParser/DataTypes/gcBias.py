#! /usr/bin/env python2.7


from .DatabaseType import DatabaseType

class gcBias(DatabaseType):
    def __init__(self, sampleID, runID, AL, ReadsUsed, GC, Windows, ReadStart, MeanBaseQuality, NormalizedCoverage, ErrorBar):
        self.sampleID = str(sampleID)
        self.runID = str(runID)
        self.ReadsUsed = str(ReadsUsed)
        self.GC = str(GC)
        self.Windows = str(Windows)
        self.ReadStart = str(ReadStart)
        self.MeanBaseQuality = str(MeanBaseQuality)
        self.NormalizedCoverage = str(NormalizedCoverage)
        self.ErrorBar = str(ErrorBar)
    
    def toDatabaseEntry(self):
        return (
            self.sampleID,
            self.runID,
            self.ReadsUsed,
            self.GC,
            self.Windows,
            self.ReadStart,
            self.MeanBaseQuality,
            self.NormalizedCoverage,
            self.ErrorBar
        )
        
