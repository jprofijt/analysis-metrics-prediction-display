#! /usr/bin/env python2.7

from __future__ import with_statement
import sqlite3, csv, sys
from .DatabaseConnector import databaseConnectorInterface
from ..DataTypes.DatabaseType import DatabaseType
from datetime import datetime

class sqlite3Database(databaseConnectorInterface):
    def __init__(self, databasefile):
        self.connection = sqlite3.connect(databasefile)
        self.cursor = self.connection.cursor()
    
    def addEntry(self, Table, Row):
        """Adds an entry to the database

            Parameters:
            Table (string): table identifier
            Row (string): items to add to table

        """
        self.cursor.execute("INSERT INTO {0} VALUES (?{1})".format(Table, (len(Row) - 1) * ',?'), Row)
        self.connection.commit()

    def addLargeEntry(self, Table, RowList):
         """Adds multiple entries to the database

            Parameters:
            Table (string): table identifier
            RowList (List): items to add to table

        """
        self.cursor.executemany("INSERT INTO {0} VALUES (?{1})".format(Table, (len(RowList[0]) - 1) * ',?'), RowList)
        self.connection.commit()

    def addSample(self, sample):
         """Adds an sample to the database

            Parameters:
            sample(sample): sample to insert 

        """
        self.cursor.execute("SELECT ID FROM Projects WHERE ID=?", (sample.Project,)) # gets the project id
        projects = self.cursor.fetchall()

        if len(projects) == 0: # if it doesnt exist add the project
            self.addProject(sample.Project)
        
        self.cursor.execute("SELECT ID FROM Sequencers WHERE ID = ?", (sample.Sequencer,)) # retrieves the sequencer used if it exists
        sequencerQuery = self.cursor.fetchall()

        if len(sequencerQuery) == 0: # if not add to database
            self.addSequencer(sample.Sequencer)
        
        self.cursor.execute("SELECT ID FROM CapturingKits WHERE ID = ?", (sample.CapturingKit,)) # retrieves the capturing kits used
        capturingKits = self.cursor.fetchall()

        if len(capturingKits) == 0: # if non existing add to database
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
         """Adds an capturing kit to the database

            Parameters:
            id (string): capturing kit id
            startDate (date): start usage date
            endDate (date): end usage date

        """
        self.addEntry("CapturingKits", (id,str(startDate), str(endDate)))
        return 0

    def addHsMetric(self, HsMetric):
        self.addEntry('hsMetrics', HsMetric.toDatabaseEntry())
        return 0
    
    def addInsertSizeEntry(self, InsertSizeMetric):
        self.addEntry('InsertSizes', InsertSizeMetric.toDatabaseEntry())
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

    def addSequencingRun(self, run):
        self.cursor.execute("INSERT INTO RUNS (RunID,Number,Flowcell,Sequencer,Date) VALUES (?,?,?,?,?)", run.toDatabaseEntry())
        self.connection.commit()
        return self.cursor.lastrowid

    def addRunSummary(self, ID, Summary):
        self.addEntry("RunSummary", Summary.toDatabaseEntry() + (ID,))
    
    def addLane(self, ID, lane):
        #self.cursor.execute("INSERT INTO Lanes (ReadID, Lane, Tiles, DensityMIN, DensityMAX, ClusterMIN,ClusterMAX,LegacyPhasing,LegacyPrephasing, PhasingSlope, PhasingOffset,PrePhasingSlope,PrePhasingOffset,Reads,ReadsPF,Q30,IntensityMIN,IntensityMAX,UniqueID) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", lane.toDatabaseEntry() + (ID,))
        #self.connection.commit()
        self.addEntry("Lanes", lane.toDatabaseEntry() + (ID,))
    
    def exit(self):
        self.connection.close()
