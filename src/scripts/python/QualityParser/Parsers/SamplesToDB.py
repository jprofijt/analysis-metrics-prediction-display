#! /usr/bin/env python2.7
from __future__ import absolute_import
import sys

from .Samples import parseArguments, parseSampleSheet, copyToFailed
from ..DataBase.SQLiteDatabaseConnector import sqlite3Database as DataBase

def IndexSamplesToDB(sampleSheet, database, failDirectory):
    try:
        samples = parseSampleSheet(sampleSheet)
        for sample in samples:
            print(sample.toList())
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
    



