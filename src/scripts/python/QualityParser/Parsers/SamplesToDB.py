#! /usr/bin/env python2.7
from __future__ import absolute_import
import sys

from .Samples import parseArguments, parseSampleSheet, copyToFailed
from ..DataBase.SQLiteDatabaseConnector import sqlite3Database as DataBase

def IndexSamplesToDB(sampleSheet, database, failDirectory):
    """Inserts samplesheets to the database

    Parameters:
    sampleSheet (string): path to samplesheet
    database (databaseConnector): database connector
    failDirectory (string): path to send failed samplesheet for further manual inspection
    
   """
    try:
        samples = parseSampleSheet(sampleSheet)
        for sample in samples:
            database.addSample(sample)
    except Exception:
        copyToFailed(sampleSheet, failDirectory)
    return 0


def main():
    args = parseArguments()
    dbc = DataBase(args.getOutput())
    IndexSamplesToDB(args.getInput(), dbc, args.getFailLocation())
    dbc.exit()
    return 0

if __name__ == '__main__':
    main()
    



