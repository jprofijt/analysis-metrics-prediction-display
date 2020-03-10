from __future__ import absolute_import, with_statement
import csv
from .parserTools import decomment, createQuickParser
from ..DataTypes.Files import Files
from ..DataTypes.InsertSizeMetric import InsertSizeMetric
from ..DataBase.SQLiteDatabaseConnector import sqlite3Database as DataBase

def parseInserSizeMetricsFile(file, sampleID, RunID):
    with open(file, u"r") as InsertSizeFile:
        output = []
        head = [next(InsertSizeFile) for x in range(8)]

        reader = csv.DictReader(decomment(head), delimiter="\t")
        for row in reader:
            output.append(InsertSizeMetric(
                sampleID,
                RunID,
                row["MEDIAN_INSERT_SIZE"],  
                row["MEDIAN_ABSOLUTE_DEVIATION"],   
                row["MIN_INSERT_SIZE"],
                row["MAX_INSERT_SIZE"],
                row["MEAN_INSERT_SIZE"],    
                row["STANDARD_DEVIATION"],  
                row["READ_PAIRS"],  
                row["PAIR_ORIENTATION"],    
                row["WIDTH_OF_10_PERCENT"], 
                row["WIDTH_OF_20_PERCENT"], 
                row["WIDTH_OF_30_PERCENT"], 
                row["WIDTH_OF_40_PERCENT"], 
                row["WIDTH_OF_50_PERCENT"], 
                row["WIDTH_OF_60_PERCENT"], 
                row["WIDTH_OF_70_PERCENT"], 
                row["WIDTH_OF_80_PERCENT"], 
                row["WIDTH_OF_90_PERCENT"], 
                row["WIDTH_OF_99_PERCENT"] 
                )
            )
    return output

def insertToDB(ISlist, database):
    for IS in ISlist:
        database.addInsertSizeEntry(IS)

def main():
    parser = createQuickParser(["input", "database", "sample", "run"], "gets the HS metrics and adds them to sqlite db")
    args = parser.parse_args()
    dbc = DataBase(args.database)
    IS = parseInserSizeMetricsFile(args.input, args.sample, args.run)
    insertToDB(IS, dbc)
    dbc.exit()

if __name__ == '__main__':
    main()
