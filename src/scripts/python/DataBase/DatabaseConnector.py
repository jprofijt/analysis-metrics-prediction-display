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

    def addQualityByCycle(self, sampleID, runID, qualityMatrix):
        raise NotImplementedError

    def addInsertSizeEntry(self, Entry):
        raise NotImplementedError

    def addAlignmentSummaryEntry(self, Entry):
        raise NotImplementedError

    def addGCbiasEntry(self, Entry):
        raise NotImplementedError

    def addHsMetric(self, Entry):
        raise NotImplementedError

    def addFlagstatEntry(self, Entry):
        raise NotImplementedError

    def exit(self):
        pass

