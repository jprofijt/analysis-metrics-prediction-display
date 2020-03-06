#! /usr/bin/env python2.7
# pylint: disable=relative-beyond-top-level

from .DatabaseType import DatabaseType

class AlignmentSummaryMetrics(DatabaseType):
    def __init__(self, SampleID ,RunID ,Category ,TotalReads,PFreads,PFnoise,PFaligned,PFHQaligned,PFalignedBases,PFHQalignedBases,PFHQalignedQ20Bases,PFHQmedianMismatches,PFmismatchRate ,PFHQErrorRate ,PFindelRate ,MeanReadLenght ,ReadsAllignedInPairs,BadCycles,StrandBalance ,ChimerasPercentage ,AdapterPercentage):
        self.SampleID = str(SampleID)  
        self.RunID = str(RunID)  
        self.Category = str(Category)  
        self.TotalReads = str(TotalReads)
        self.PFreads = str(PFreads)
        self.PFnoise = str(PFnoise)
        self.PFaligned = str(PFaligned)
        self.PFHQaligned = str(PFHQaligned)
        self.PFalignedBases = str(PFalignedBases)
        self.PFHQalignedBases = str(PFHQalignedBases)
        self.PFHQalignedQ20Bases = str(PFHQalignedQ20Bases)
        self.PFHQmedianMismatches = str(PFHQmedianMismatches)
        self.PFmismatchRate = str(PFmismatchRate) 
        self.PFHQErrorRate = str(PFHQErrorRate) 
        self.PFindelRate = str(PFindelRate) 
        self.MeanReadLenght = str(MeanReadLenght) 
        self.ReadsAllignedInPairs = str(ReadsAllignedInPairs)
        self.BadCycles = str(BadCycles)
        self.StrandBalance = str(StrandBalance) 
        self.ChimerasPercentage = str(ChimerasPercentage) 
        self.AdapterPercentage = str(AdapterPercentage) 

    def toDatabaseEntry(self):
        return (
            self.SampleID,
            self.RunID,
            self.Category,
            self.TotalReads,
            self.PFreads,
            self.PFnoise,
            self.PFaligned,
            self.PFHQaligned,
            self.PFalignedBases,
            self.PFHQalignedBases,
            self.PFHQalignedQ20Bases,
            self.PFHQmedianMismatches,
            self.PFmismatchRate,
            self.PFHQErrorRate,
            self.PFindelRate,
            self.MeanReadLenght,
            self.ReadsAllignedInPairs,
            self.BadCycles,
            self.StrandBalance,
            self.ChimerasPercentage,
            self.AdapterPercentage
        )
