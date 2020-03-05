class gcBias(object):
    def __init__(self, sampleID, runID, AL, ReadsUsed, GC, Windows, ReadStart, MeanBaseQuality, NormalizedCoverage, ErrorBar):
        self.sampleID = sampleID
        self.runID = runID
        self.ReadsUsed = ReadsUsed
        self.GC = GC
        self.Windows = Windows
        self.ReadStart = ReadStart
        self.MeanBaseQuality = MeanBaseQuality
        self.NormalizedCoverage = NormalizedCoverage
        self.ErrorBar = ErrorBar
    
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
        