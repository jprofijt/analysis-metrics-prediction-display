#! /usr/bin/env python2.7
# pylint: disable=relative-beyond-top-level

from __future__ import with_statement
import sqlite3, csv, sys
from .DatabaseConnector import databaseConnectorInterface
from ..ParseQualityDistributionMetrics import QualityDistribution
from ..DataTypes.QualityPerCycle import QualityPerCycle

class sqlite3Database(databaseConnectorInterface):
    def __init__(self, databasefile):
        self.connection = sqlite3.connect(databasefile)
        self.cursor = self.connection.cursor()
    
    def addSample(self, id, sequencer, run, flowcell, startDate, project, capturingKit):
        self.cursor.execute("SELECT ID FROM Projects WHERE ID=?", (str(project),))
        projects = self.cursor.fetchall()

        if len(projects) == 0:
            self.addProject(project)
        
        self.cursor.execute("SELECT ID FROM Sequencers WHERE ID = ?", (str(sequencer),))
        sequencerQuery = self.cursor.fetchall()

        if len(sequencerQuery) == 0:
            self.addSequencer(sequencer)
        
        self.cursor.execute("SELECT ID FROM CapturingKits WHERE ID = ?", (str(capturingKit),))
        capturingKits = self.cursor.fetchall()

        if len(capturingKits) == 0:
            self.addCapturingKit(capturingKit)
        
        self.cursor.execute("INSERT INTO Samples VALUES (?,?,?,?,?,?,?)", (str(id), str(sequencer), str(run), str(flowcell), str(startDate), str(project), str(capturingKit)))
        self.connection.commit()
        return 0

    def addProject(self, project):
        self.cursor.execute("INSERT INTO Projects VALUES (?)", (str(project),))
        self.connection.commit()
        return 0

    def addSequencer(self, id):
        self.cursor.execute("INSERT INTO Sequencers VALUES (?)", (str(id),))
        self.connection.commit()
        return 0

    def addCapturingKit(self, id, startDate=u'NULL', endDate=u'NULL'):
        self.cursor.execute("INSERT INTO CapturingKits VALUES (?, ?, ?)", (str(id),str(startDate), str(endDate)))
        self.connection.commit()
        return 0
    
    def addQualityDistribution(self, QualityDistribution):
        self.cursor.executemany("INSERT INTO QualityDistributions VALUES (?,?,?)", QualityDistribution.toDatabaseEntry())
        self.connection.commit()
        return 0
    
    def addQualityByCycle(self, QualityByCycle: QualityPerCycle):
        self.cursor.executemany("INSERT INTO QualityByCycle VALUES (?,?,?,?)", QualityByCycle.toDatabaseEntry())
        self.connection.commit()
        return 0
    
    
    def exit(self):
        self.connection.close()
