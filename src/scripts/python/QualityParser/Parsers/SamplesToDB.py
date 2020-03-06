#! /usr/bin/env python2.7
from __future__ import absolute_import
import sys

from .Samples import parseArguments, parseSampleSheet, copyToFailed
from ..DataBase.SQLiteDatabaseConnector import sqlite3Database as DataBase

def IndexSamplesToDB():
    args = parseArguments()
    dbc = DataBase(args.getOutput())
    try:
        samples = parseSampleSheet(args.getInput())
        for sample in samples:
            dbc.addSample(sample)
    except Exception:
        copyToFailed(args.getInput(), args.getFailLocation())
    finally:
        dbc.exit()
    
    return 0

if __name__ == "__main__":
    sys.exit(IndexSamplesToDB())

