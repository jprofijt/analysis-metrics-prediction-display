#! /usr/bin/env python2.7

from __future__ import with_statement
import sqlite3, csv, sys
from .DatabaseConnector import databaseConnectorInterface
from ..DataTypes.DatabaseType import DatabaseType

class sqlite3Database(databaseConnectorInterface):
    def __init__(self, databasefile):
        self.connection = sqlite3.connect(databasefile)
        self.cursor = self.connection.cursor()
    
    def addEntry(self, Table, Row):
        self.cursor.execute("INSERT INTO {0} VALUES (?{1})".format(Table, (len(Row) - 1) * ',?'), Row)
        self.connection.commit()

    def addLargeEntry(self, Table, RowList):
        self.cursor.executemany("INSERT INTO {0} VALUES (?{1})".format(Table, (len(RowList[0]) - 1) * ',?'), RowList)
        self.connection.commit()

    def addSample(self, sample):
        self.cursor.execute("SELECT ID FROM Projects WHERE ID=?", (sample.Project,))
        projects = self.cursor.fetchall()

        if len(projects) == 0:
            self.addProject(sample.Project)
        
        self.cursor.execute("SELECT ID FROM Sequencers WHERE ID = ?", (sample.Sequencer,))
        sequencerQuery = self.cursor.fetchall()

        if len(sequencerQuery) == 0:
            self.addSequencer(sample.Sequencer)
        
        self.cursor.execute("SELECT ID FROM CapturingKits WHERE ID = ?", (sample.CapturingKit,))
        capturingKits = self.cursor.fetchall()

        if len(capturingKits) == 0:
            self.addCapturingKit(sample.CapturingKit)
        
        try:
            self.addEntry('Samples', sample.toDatabaseEntry())
        except sqlite3.IntegrityError:
            pass
        return 0

    def addProject(self, project):
        self.addEntry('Projects', (project,))
        return 0

    def addSequencer(self, id):
        self.addEntry('Sequencers', (id,))
        return 0

    def addCapturingKit(self, id, startDate=u'NULL', endDate=u'NULL'):
        self.addEntry("CapturingKits", (id,str(startDate), str(endDate)))
        return 0
    
    def addAlignmentSummaryEntry(self, AlignmentSummaryMetrics):
        self.addEntry('AlignmentSummaryMetrics', AlignmentSummaryMetrics.toDatabaseEntry())
        return 0
    
    def addFlagstatEntry(self, FlagstatMetric):
        self.addEntry('FlagstatMetrics', FlagstatMetric.toDatabaseEntry())
        return 0
    
    def addGCbiasEntry(self, gcBias):
        self.addEntry('GCBiasMetrics', gcBias.toDatabaseEntry())
        return 0
    
    def addQualityDistribution(self, QualityDistribution):
        self.addLargeEntry("QualityDistributions", QualityDistribution.toDatabaseEntry())
        return 0
    
    def addQualityByCycle(self, QualityByCycle):
        self.addLargeEntry("QualityByCycle", QualityByCycle.toDatabaseEntry())
        return 0
    
    
    def exit(self):
        self.connection.close()
