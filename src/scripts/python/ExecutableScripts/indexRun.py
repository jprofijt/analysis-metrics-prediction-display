#! /usr/bin/env python2.7
import os, argparse, sys
import QualityParser as QP

def indexRun(runDir, runID, database):
    for filename in os.listdir(runDir):
        fullpath = os.path.join(runDir, filename)
        splitFilename = filename.split(".")
        filetype = splitFilename[-1]
        sampleID = splitFilename[0]
        try:
            if filetype == "alignment_summary_metrics":
                QP.insertASMtoDB(QP.parseAlignmentSummaryMetirics(fullpath, sampleID, runID), database)
            elif filetype == "flagstat":
                QP.insertFlagstatToDB(QP.parseFlagstatFile(fullpath, sampleID, runID), database)
            elif filetype == "gc_bias_metrics":
                QP.insertGcToDB(QP.parseGcBiasFile(fullpath, sampleID, runID), database)
            elif filetype == "insert_size_metrics":
                QP.insertInsertSizeToDB(QP.parseInserSizeMetricsFile(fullpath, sampleID, runID), database)
            elif filetype == "hs_metrics":
                QP.insertHsToDB(QP.parseHsMetricsFile(fullpath, sampleID, runID), database)
            elif filetype == "quality_by_cycle_metrics":
                QP.insertQBCtoDB(QP.QBCparser(fullpath, sampleID, runID), database)
            elif filetype == "quality_distribution":
                QP.insertQDMtoDB(QP.parseQDM(fullpath, sampleID, runID), database)
            else:
                continue
        except Exception as e:
            addExceptionLog(database, filetype, sampleID, runID, str(e))

def addExceptionLog(database, type, sample, run, exception):
    database.addEntry('LOG', "Failed parsing {0} for {1} in run {2}. Error: {3}".format(type, sample, run, exception))

def createQuickParser(args, description):
    parser = argparse.ArgumentParser(description=description)
    for item in args:
        parser.add_argument(u"-{0}".format(item[0]), u"--{0}".format(item), type=unicode, required=True)
    
    return parser

def main():
    parser = createQuickParser(["rundir", "database", "id"], "indexes metric files in run folder")

    args = parser.parse_args()

    database = QP.sqlite3Database(args.database)
    try:
        indexRun(args.rundir, args.id, database)
    finally:
        database.exit()
    return 0

if __name__ == "__main__":
    sys.exit(main())

            



