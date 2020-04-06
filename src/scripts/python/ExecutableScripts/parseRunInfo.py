#! /usr/bin/env python2
from __future__ import absolute_import
import sys
sys.path.append("/home/jouke/Analysis-Metrics-Prediction/src/scripts/python/")
import xml.etree.ElementTree as ET
import subprocess

import QualityParser as QP

import argparse
import datetime

def dateParser(dateString):
    return datetime.datetime.strptime(dateString, "%y%m%d").date()

def parseRun(xml):
    tree = ET.parse(xml)

    root = tree.getroot()


    run = root.find("Run")
    number = root.get("Number")
    FlowCell = run.find("Flowcell")
    Sequencer = run.find("Instrument")
    Date = run.find("Date")
    return QP.SequencingRun(run.attrib["Id"], run.attrib["Number"], FlowCell.text, Sequencer.text, dateParser(Date.text.strip()))
    
def parseInteropSummary(interop, summaryApplication):
    summary = subprocess.check_output([summaryApplication, interop, '--level=3', '--csv=1']).split('\n')
    counter = 0
    stored = []
    lanes = []
    for line in summary:
        row = line.split(",")
        if line.startswith("#") or len(row) == 0:
            continue
        elif len(row) == 1:
            counter = 1
            tableHeader = row[0]
        else:
            if tableHeader == "Info" and "Read" in row[0]:
                stored.append(QP.Summary(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                ))
            elif "Read" in tableHeader and row[0].isdigit():
                read = str(tableHeader)
                lane = int(row[0])
                tiles = int(row[2])
                density = splitInteropType(row[3])
                clusterPF = splitInteropType(row[4])
                LegacyPhasing = row[5].split("/")
                PhasingSlopeOffset = row[6].split("/")
                PrephasingSlopeOffset = row[7].split("/")
                reads = float(row[8])
                readsPF = float(row[9])
                Q30 = float(row[10])
                intensity = splitInteropType(row[-1])
                lanes.append(QP.Lane(
                    read,
                    lane,
                    tiles,
                    float(density["min"]),
                    float(density["max"]),
                    float(clusterPF["min"]),
                    float(clusterPF["max"]),
                    float(LegacyPhasing[0]), # phasing
                    float(LegacyPhasing[1]), # prephasing
                    float(PhasingSlopeOffset[0]), # Slope
                    float(PhasingSlopeOffset[1]), # Offset
                    float(PrephasingSlopeOffset[0]), # Slope
                    float(PrephasingSlopeOffset[1]), # Offset
                    reads,
                    readsPF,
                    Q30,
                    int(intensity["min"]),
                    int(intensity["max"])
                ))
            counter += 1
    return {"summarys": stored, "lanes": lanes} 


def insertToDB(runInfo, summarys, lanes, database):
    RunID = database.addSequencingRun(runInfo)
    for summary in summarys:
        database.addRunSummary(RunID, summary)
    for lane in lanes:
        database.addLane(RunID, lane)
    

def createQuickParser(args, description):
    parser = argparse.ArgumentParser(description=description)
    for item in args:
        parser.add_argument(u"-{0}".format(item[0]), u"--{0}".format(item), type=unicode, required=True)
    
    return parser

def splitInteropType(string):
    split = string.split("+/-")
    d = {
        "min": split[1].strip(),
        "max": split[0].strip()
    }
    return d

def main():
    
    parser = createQuickParser(["runxml", "interop", "database", "executable"], "Parser for interop folders, inserts run summary to database")
    args = parser.parse_args()
    runInfo = parseRun(args.runxml)
    data = parseInteropSummary(args.interop, args.executable)
    database = QP.sqlite3Database(args.database)
    insertToDB(runInfo, data["summarys"], data["lanes"], database)
    return 0

if __name__ == "__main__":
    sys.exit(main())