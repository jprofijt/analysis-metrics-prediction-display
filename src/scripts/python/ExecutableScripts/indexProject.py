#! /usr/bin/env python

import os, argparse, sys
import QualityParser as QP
from indexRun import indexRun

def indexProject(directory, database, projectID):
    runs = [o for o in os.listdir(directory) if os.path.isdir(os.path.join(directory,o))]
    
    for run in runs:
        path = os.path.join(directory, run)
        statsDir = os.path.join(path, 'results/qc/statistics')
        sampleSheet = os.path.join(path, 'results/', "{0}.csv".format(projectID))
        if os.path.isdir(statsDir) and os.path.isfile(sampleSheet):
            QP.IndexSamplesToDB(sampleSheet, database, "/tmp/failedSampleSheets/")
            indexRun(statsDir, run, database)



def createQuickParser(args, description):
    parser = argparse.ArgumentParser(description=description)
    for item in args:
        parser.add_argument(u"-{0}".format(item[0]), u"--{0}".format(item), type=unicode, required=True)
    
    return parser

def main():
    parser = createQuickParser(["projectdir", "database", "id"], "indexes metric files in project folder")

    args = parser.parse_args()

    database = QP.sqlite3Database(args.database)
    try:
        indexProject(args.projectdir, database, args.id)
    finally:
        database.exit()
    return 0

if __name__ == "__main__":
    sys.exit(main())



        