#! /usr/bin/env python2

from __future__ import absolute_import, with_statement
import csv
from .parserTools import decomment, createQuickParser
from ..DataTypes.Files import Files
from ..DataTypes.FlagstatMetrics import FlagstatMetric
from ..DataBase.SQLiteDatabaseConnector import sqlite3Database as DataBase

class IncompatibleFlagstatFile(Exception):
    pass


def parseFlagstatRow(row, outputList):
    split = row.split(" ")
    outputList.append(split[0])
    outputList.append(split[2])
    if ("mapped" in row and "mate" not in row) or "singletons" in row or "properly" in row:
        percent = split[-1].strip().replace("%:N/A)", "").replace("(", "")
        outputList.append(percent)
    return outputList


def parseFlagstatFile(file, sampleID, RunID):
    output = []
    with open(file, u'r') as flagstatFile:
        for row in flagstatFile:
            output = parseFlagstatRow(row, output)
    if len(output) != 29:
        raise IncompatibleFlagstatFile()
    # pylint: disable=no-value-for-parameter
    return FlagstatMetric(sampleID, RunID, *output)

def insertToDB(FlMetrics, database):
    database.addFlagstatEntry(FlMetrics)


def main():
    parser = createQuickParser(["input", "database", "sample", "run"], "gets the flagstat metrics and adds them to sqlite db")
    args = parser.parse_args()
    dbc = DataBase(args.database)
    FL = parseFlagstatFile(args.input, args.sample, args.run)
    insertToDB(FL, dbc)
    dbc.exit()

if __name__ == '__main__':
    main()
    


