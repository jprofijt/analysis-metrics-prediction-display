import itertools

class QualityPerCycle(object):
    def __init__(self, SampleID, RunID, cycles, quality):
        self.sampleID = SampleID
        self.runID = RunID
        self.cycles = cycles
        self.quality = quality
    
    def toDatabaseEntry(self):
        output = []
        for cycle, quality in itertools.zip_longest(self.cycles, self.quality):
            output.append((self.sampleID, self.runID, cycle, quality))
        return output

        
    