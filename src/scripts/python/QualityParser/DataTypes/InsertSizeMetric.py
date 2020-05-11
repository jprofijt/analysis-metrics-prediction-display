#! /usr/bin/env python2.7

from .DatabaseType import DatabaseType

class InsertSizeMetric(DatabaseType):
    def __init__(self,SampleID ,RunID ,MedianSize,MedianAbsoluteDeviation,MinSize,MaxSize,MeanSize,StandardDeviation ,ReadPairs,PairOrientation ,W10,W20,W30,W40,W50,W60,W70,W80,W90,W99):
        self.SampleID = str(SampleID)  
        self.RunID = str(RunID)  
        self.MedianSize = str(MedianSize)
        self.MedianAbsoluteDeviation = str(MedianAbsoluteDeviation)
        self.MinSize = str(MinSize)
        self.MaxSize = str(MaxSize)
        self.MeanSize = str(MeanSize)
        self.StandardDeviation = str(StandardDeviation)
        self.ReadPairs = str(ReadPairs)
        self.PairOrientation = str(PairOrientation)  
        self.W10 = str(W10)
        self.W20 = str(W20)
        self.W30 = str(W30)
        self.W40 = str(W40)
        self.W50 = str(W50)
        self.W60 = str(W60)
        self.W70 = str(W70)
        self.W80 = str(W80)
        self.W90 = str(W90)
        self.W99 = str(W99)

    def toDatabaseEntry(self):
        return (
            self.SampleID,
            self.RunID,
            self.MedianSize,
            self.MedianAbsoluteDeviation,
            self.MinSize,
            self.MaxSize,
            self.MeanSize,
            self.StandardDeviation,
            self.ReadPairs,
            self.PairOrientation,
            self.W10,
            self.W20,
            self.W30,
            self.W40,
            self.W50,
            self.W60,
            self.W70,
            self.W80,
            self.W90,
            self.W99
        )
