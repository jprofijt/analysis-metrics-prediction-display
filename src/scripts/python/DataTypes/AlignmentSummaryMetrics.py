class AlignmentSummaryMetrics(object):
    def __init__(self, SampleID ,RunID ,Category ,TotalReads,PFreads,PFnoise,PFaligned,PFHQaligned,PFalignedBases,PFHQalignedBases,PFHQalignedQ20Bases,PFHQmedianMismatches,PFmismatchRate ,PFHQErrorRate ,PFindelRate ,MeanReadLenght ,ReadsAllignedInPairs,BadCycles,StrandBalance ,ChimerasPercentage ,AdapterPercentage):
        self.SampleID = SampleID  
        self.RunID = RunID  
        self.Category = Category  
        self.TotalReads = TotalReads
        self.PFreads = PFreads
        self.PFnoise = PFnoise
        self.PFaligned = PFaligned
        self.PFHQaligned = PFHQaligned
        self.PFalignedBases = PFalignedBases
        self.PFHQalignedBases = PFHQalignedBases
        self.PFHQalignedQ20Bases = PFHQalignedQ20Bases
        self.PFHQmedianMismatches = PFHQmedianMismatches
        self.PFmismatchRate = PFmismatchRate 
        self.PFHQErrorRate = PFHQErrorRate 
        self.PFindelRate = PFindelRate 
        self.MeanReadLenght = MeanReadLenght 
        self.ReadsAllignedInPairs = ReadsAllignedInPairs
        self.BadCycles = BadCycles
        self.StrandBalance = StrandBalance 
        self.ChimerasPercentage = ChimerasPercentage 
        self.AdapterPercentage = AdapterPercentage 

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
