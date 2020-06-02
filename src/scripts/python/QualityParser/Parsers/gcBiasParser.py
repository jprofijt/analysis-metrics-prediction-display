from __future__ import absolute_import, with_statement
import csv
from .parserTools import decomment, createQuickParser
from ..DataTypes.Files import Files
from ..DataTypes.gcBias import gcBias
from ..DataBase.SQLiteDatabaseConnector import sqlite3Database as DataBase

def parseGcBiasFile(file, sampleID, RunID):
    """Parses gc bias file

    Parameters:
    file (string): GC bias file path
    sampleID (string): sample ID
    RunID (string): Run ID

    Returns:
    List:parsed gc bias information

   """
    with open(file, u"r") as gcBiasFile:
        output = []
        reader = csv.DictReader(decomment(gcBiasFile), delimiter="\t")
        for row in reader:
            output.append(gcBias(
                sampleID,
                RunID,
                row["ACCUMULATION_LEVEL"],  
                row["READS_USED"],  
                row["GC"],  
                row["WINDOWS"],
                row["READ_STARTS"], 
                row["MEAN_BASE_QUALITY"],   
                row["NORMALIZED_COVERAGE"], 
                row["ERROR_BAR_WIDTH"]
                )
            )
    return output

def insertToDB(gcList, database):
    """Inserts gcBias data into database

    Parameters:
    gcList (List): List of rows to add
    database (databaseConnector): database connector
    
   """
    for gc in gcList:
        database.addGCbiasEntry(gc)

def main():
    parser = createQuickParser(["input", "database", "sample", "run"], "gets the GCBias metrics and adds them to sqlite db")
    args = parser.parse_args()
    dbc = DataBase(args.database)
    GC = parseGcBiasFile(args.input, args.sample, args.run)
    insertToDB(GC, dbc)
    dbc.exit()

if __name__ == '__main__':
    main()



