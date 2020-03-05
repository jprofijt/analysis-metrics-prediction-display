#! /usr/bin/env python2.7
# pylint: disable=relative-beyond-top-level
from ..DataTypes.QualityPerCycle import QualityPerCycle
from ..DataTypes.gcBias import gcBias

class databaseConnectorInterface(object):
    def addSample(self, id, sequencer, run, flowcell, startDate, project, capturingKit):
        raise NotImplementedError

    def addProject(self, id):
        raise NotImplementedError

    def addSequencer(self, id):
        raise NotImplementedError

    def addCapturingKit(self, id, startDate = None, endDate = None):
        raise NotImplementedError

    def addQualityDistribution(self, QualityDistribution):
        raise NotImplementedError

    def addQualityByCycle(self, QualityByCycleObject): # type: (databaseConnectorInterface, QualityPerCycle) -> int
        raise NotImplementedError

    def addInsertSizeEntry(self, Entry):
        raise NotImplementedError

    def addAlignmentSummaryEntry(self, Entry):
        raise NotImplementedError

    def addGCbiasEntry(self, gcBias):
        raise NotImplementedError

    def addHsMetric(self, Entry):
        raise NotImplementedError

    def addFlagstatEntry(self, Entry):
        raise NotImplementedError

    def exit(self):
        pass

