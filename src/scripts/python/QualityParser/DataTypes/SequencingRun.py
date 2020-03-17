#! /usr/bin/env python2

from .DatabaseType import DatabaseType

class SequencingRun(DatabaseType):
    def __init__(self, runId, Number, Flowcell, Date):
        self.runID = runId
        self.Number = Number
        self.Flowcell = Flowcell
        self.Date = Date
    
    def toDatabaseEntry(self):
        return (
            self.runID,
            self.Number,
            self.Flowcell,
            self.Date
        )
        