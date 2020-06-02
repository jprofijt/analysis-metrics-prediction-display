#! /usr/bin/env python2.7

from __future__ import absolute_import, with_statement
import csv
from .parserTools import decomment, createQuickParser
from ..DataTypes.Files import Files
from ..DataTypes.AlignmentSummaryMetrics import AlignmentSummaryMetrics
from ..DataBase.SQLiteDatabaseConnector import sqlite3Database as DataBase


def parseAlignmentSummaryMetirics(file, sampleID, runID):
     """Parses AlignmentSummaryMetrics files

        Parameters:
        file (string): file to parse
        sampleID (string): sampleID for file
        runID (string): runID to which the sample and file belongs

        Returns:
        ListOfEntries (List): List of AlignmentSummaryMetrics objects

    """
    output = []
    with open(file, u'r') as ASM:
        reader = csv.DictReader(decomment(ASM), delimiter='\t')
        for row in reader:
            output.append(
                AlignmentSummaryMetrics(
                    sampleID,
                    runID,
                    row["CATEGORY"],
                    row["TOTAL_READS"],
                    row["PF_READS"],
                    row["PF_NOISE_READS"],
                    row["PF_READS_ALIGNED"],
                    row["PF_ALIGNED_BASES"],    
                    row["PF_HQ_ALIGNED_READS"], 
                    row["PF_HQ_ALIGNED_BASES"], 
                    row["PF_HQ_ALIGNED_Q20_BASES"],
                    row["PF_HQ_MEDIAN_MISMATCHES"],
                    row["PF_MISMATCH_RATE"],    
                    row["PF_HQ_ERROR_RATE"],    
                    row["PF_INDEL_RATE"],
                    row["MEAN_READ_LENGTH"],    
                    row["READS_ALIGNED_IN_PAIRS"],  
                    row["BAD_CYCLES"],  
                    row["STRAND_BALANCE"],
                    row["PCT_CHIMERAS"],
                    row["PCT_ADAPTER"]
                )
            )

    return output


def insertToDB(listOfEntries, database):
     """Adds an ASM entry to the database

            Parameters:
            ListofEntries (List): List of AlignmentSummaryMetrics objects
            database (databaseConnector): database connector

        """
    for ASM in listOfEntries:
        database.addAlignmentSummaryEntry(ASM)


def main():
    parser = createQuickParser(["input", "database", "sample", "run"], "gets the alignment summary metrics and adds them to sqlite db")
    args = parser.parse_args()
    dbc = DataBase(args.database)
    ASMList = parseAlignmentSummaryMetirics(args.input, args.sample, args.run)
    for ASM in ASMList:
        dbc.addAlignmentSummaryEntry(ASM)
    dbc.exit()
if __name__ == '__main__':
    main()
    

                




