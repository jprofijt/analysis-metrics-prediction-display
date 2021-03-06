#! /usr/bin/env python2.7
#! /usr/bin/env python2.7
# pylint: disable=relative-beyond-top-level

from __future__ import with_statement
from __future__ import absolute_import
import csv, os, argparse, sys, shutil
from ..DataTypes.Files import Files
from ..DataTypes.QualityDistribution import QualityDistribution
from .parserTools import decomment
from io import open
from ..DataBase.SQLiteDatabaseConnector import sqlite3Database as DataBase


class FileArguments(Files):
    def __init__(self, input, output, sampleID, runID):
        Files.__init__(self, input, output)
        self.sample = sampleID
        self.run = runID
    
    def getSampleID(self):
        return self.sample
    
    def getRunID(self):
        return self.run


def parseArguments():
    # pylint: disable=undefined-variable
    parser = argparse.ArgumentParser(description=u'Parses sample sheet and adds to output file')
    parser.add_argument(u'-i', u'--input', type=unicode, metavar="path/to/input", help=u'Sample sheet to read', required=True)
    parser.add_argument(u'-o', u'--output', type=unicode, metavar="path/to/output", help=u'file to add results to', required=True)
    parser.add_argument(u'-s', u'--sampleid', type=unicode, metavar="SAMPLEID", help=u'Sample id to use', required=True)
    parser.add_argument(u'-r', u'--runid', type=unicode, metavar="RUNID", help=u'Run identifier', required=True)
    args = parser.parse_args()
    files = FileArguments(args.input, args.output, args.sampleid, args.runid)
    return files


def parseQDM(qd, input):
    """Parses Quality distribution metrics file, per quality bin

    Parameters:
    qd (QualityDistribution): Quality Distribution class to add bins to
    input (string): Quality distribution file path

    Returns:
    QualityDistribution: class to hold quality bins
   """
    with open(input, u'r') as qdm:
        reader = csv.DictReader(decomment(qdm), delimiter="\t")
        for row in reader:
           qd.addQualityBin(row["QUALITY"], row["COUNT_OF_Q"])
    return qd

def writeToCsv(qd, output):
    """Writes Quality distribution to csv

    Parameters:
    qd (QualityDistribution): Quality distribution class
    output (string): path to output csv
    
   """
    openType = u'ab'
    if not os.path.exists(output):
        openType = u'wb'

    with open(output, openType) as csvFile:
        row = [qd.getRunID(), qd.getSampleID()] + qd.toList()
        csv.writer(csvFile).writerow(row)

def writeToDB(qd, database):
    """Inserts Quality Distribution data into database

    Parameters:
    qd (QualityDistribution): Quality distribution class
    database (databaseConnector): database connector
    
   """
    database.addQualityDistribution(qd)
def main():
    args = parseArguments()
    qd = QualityDistribution(args.getRunID(), args.getSampleID())
    qd = parseQDM(qd, args.getInput())
    dbc = DataBase(args.getOutput())
    writeToDB(qd, dbc)
    dbc.exit()
    return 0

if __name__ == "__main__":
    sys.exit(main())

