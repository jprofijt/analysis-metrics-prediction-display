class InsertSizeMetric(object):
    def __init__(self,SampleID ,RunID ,MedianSize,MedianAbsoluteDeviation,MinSize,MaxSize,MeanSize,StandardDeviation ,ReadPairs,PairOrientation ,W10,W20,W30,W40,W50,W60,W70,W80,W90,W99):
        self.SampleID = SampleID  
        self.RunID = RunID  
        self.MedianSize = MedianSize
        self.MedianAbsoluteDeviation = MedianAbsoluteDeviation
        self.MinSize = MinSize
        self.MaxSize = MaxSize
        self.MeanSize = MeanSize
        self.StandardDeviation = StandardDeviation
        self.ReadPairs = ReadPairs
        self.PairOrientation = PairOrientation  
        self.W10 = W10
        self.W20 = W20
        self.W30 = W30
        self.W40 = W40
        self.W50 = W50
        self.W60 = W60
        self.W70 = W70
        self.W80 = W80
        self.W90 = W90
        self.W99 = W99

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
