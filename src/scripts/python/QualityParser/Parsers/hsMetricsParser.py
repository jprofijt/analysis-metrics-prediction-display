from __future__ import absolute_import, with_statement
import csv
from .parserTools import decomment, createQuickParser
from ..DataTypes.Files import Files
from ..DataTypes.hsMetrics import hsMetric
from ..DataBase.SQLiteDatabaseConnector import sqlite3Database as DataBase

def parseHsMetricsFile(file, sampleID, RunID):
    with open(file, u"r") as hsFile:
        output = []
        head = [next(hsFile) for x in range(9)]

        reader = csv.DictReader(decomment(head), delimiter="\t")
        for row in reader:
            output.append(
                hsMetric(
                sampleID, 
                RunID,
                row["BAIT_SET"],    
                row["GENOME_SIZE"], 
                row["BAIT_TERRITORY"],
                row["TARGET_TERRITORY"],    
                row["BAIT_DESIGN_EFFICIENCY"],
                row["TOTAL_READS"], 
                row["PF_READS"],    
                row["PF_UNIQUE_READS"],
                row["PF_UQ_READS_ALIGNED"], 
                row["PF_BASES_ALIGNED"],    
                row["PF_UQ_BASES_ALIGNED"], 
                row["ON_BAIT_BASES"],
                row["NEAR_BAIT_BASES"],
                row["OFF_BAIT_BASES"],
                row["ON_TARGET_BASES"],
                row["PCT_SELECTED_BASES"],
                row["ON_BAIT_VS_SELECTED"], 
                row["MEAN_BAIT_COVERAGE"],  
                row["MEAN_TARGET_COVERAGE"],
                row["MEDIAN_TARGET_COVERAGE"],
                row["PCT_USABLE_BASES_ON_BAIT"],    
                row["PCT_USABLE_BASES_ON_TARGET"],  
                row["FOLD_ENRICHMENT"],
                row["ZERO_CVG_TARGETS_PCT"],
                row["PCT_EXC_DUPE"],
                row["PCT_EXC_MAPQ"],
                row["PCT_EXC_BASEQ"],
                row["PCT_EXC_OVERLAP"],
                row["PCT_EXC_OFF_TARGET"],  
                row["FOLD_80_BASE_PENALTY"],
                row["PCT_TARGET_BASES_1X"], 
                row["PCT_TARGET_BASES_2X"], 
                row["PCT_TARGET_BASES_10X"],
                row["PCT_TARGET_BASES_20X"],
                row["PCT_TARGET_BASES_30X"],
                row["PCT_TARGET_BASES_40X"],
                row["PCT_TARGET_BASES_50X"],
                row["PCT_TARGET_BASES_100X"],
                row["HS_LIBRARY_SIZE"],
                row["HS_PENALTY_10X"],
                row["HS_PENALTY_20X"],
                row["HS_PENALTY_30X"],
                row["HS_PENALTY_40X"],
                row["HS_PENALTY_50X"],
                row["HS_PENALTY_100X"],
                row["AT_DROPOUT"],  
                row["GC_DROPOUT"],
                row["HET_SNP_SENSITIVITY"], 
                row["HET_SNP_Q"]   
                )
            )
    return output

def insertToDB(HSlist, database):
    for HS in HSlist:
        database.addHsMetric(HS)

def main():
    parser = createQuickParser(["input", "database", "sample", "run"], "gets the HS metrics and adds them to sqlite db")
    args = parser.parse_args()
    dbc = DataBase(args.database)
    HS = parseHsMetricsFile(args.input, args.sample, args.run)
    insertToDB(HS, dbc)
    dbc.exit()

if __name__ == '__main__':
    main()