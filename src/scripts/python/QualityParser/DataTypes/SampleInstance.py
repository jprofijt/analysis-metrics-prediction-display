#! /usr/bin/env python2.7

from .DatabaseType import DatabaseType

class SampleObject(DatabaseType):
    def __init__(self, SampleID, sequencer, run, flowcell, startDate, project, capturingKit):
        self.SampleID = str(SampleID)
        self.Sequencer = str(sequencer)
        self.Run = str(run)
        self.Flowcell = str(flowcell)
        self.startDate = startDate
        self.Project = str(project)
        self.CapturingKit = str(capturingKit)
    
    def toDatabaseEntry(self):
        return (
            self.SampleID,
            self.Sequencer,
            self.Run,
            self.Flowcell,
            self.startDate,
            self.Project,
            self.CapturingKit
        )
    def toList(self):
        return [
            self.SampleID,
            self.Sequencer,
            self.Run,
            self.Flowcell,
            self.startDate,
            self.Project,
            self.CapturingKit
        ]