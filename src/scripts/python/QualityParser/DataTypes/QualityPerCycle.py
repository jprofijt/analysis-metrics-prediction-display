#! /usr/bin/env python2.7

import itertools
from .DatabaseType import DatabaseType

class QualityPerCycle(DatabaseType):
    def __init__(self, SampleID, RunID, cycles, quality):
        self.sampleID = SampleID
        self.runID = RunID
        self.cycles = cycles
        self.quality = quality
    
    def toDatabaseEntry(self):
        output = []
        for cycle, quality in itertools.zip_longest(self.cycles, self.quality):
            output.append((str(self.sampleID), str(self.runID), str(cycle), str(quality)))
        return output

        
    
