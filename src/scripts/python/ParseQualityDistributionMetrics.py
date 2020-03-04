#! /usr/bin/env python2.7

from __future__ import with_statement
from __future__ import absolute_import
import csv, os, argparse, sys, shutil
from InputFiles import Files
from io import open

class FileArguments(Files):
    def __init__(self, input, output, sampleID, runID):
        Files.__init__(self, input, output)
        self.sample = sampleID
        self.run = runID
    
    def getSampleID(self):
        return self.sample
    
    def getRunID(self):
        return self.run



def parseArguments():
    # pylint: disable=undefined-variable
    parser = argparse.ArgumentParser(description=u'Parses sample sheet and adds to output file')
    parser.add_argument(u'-i', u'--input', type=unicode, metavar="path/to/input", help=u'Sample sheet to read', required=True)
    parser.add_argument(u'-o', u'--output', type=unicode, metavar="path/to/output", help=u'file to add results to', required=True)
    parser.add_argument(u'-s', u'--sampleid', type=unicode, metavar="SAMPLEID", help=u'Sample id to use', required=True)
    parser.add_argument(u'-r', u'--runid', type=unicode, metavar="RUNID", help=u'Run identifier', required=True)
    args = parser.parse_args()
    files = FileArguments(args.input, args.output, args.sampleid, args.runid)
    return files

def decomment(csvfile):
    for row in csvfile:
        raw = row.split(u'#')[0].strip()
        if raw: yield raw

def parseQDM(input):
    qualityDistribution = {}
    with open(input, u'r') as qdm:
        reader = csv.DictReader(decomment(qdm), delimiter="\t")
        for row in reader:
            qualityDistribution[row[u'QUALITY']] = row[u'COUNT_OF_Q']
    return qualityDistribution

def main():
    args = parseArguments()
    runs = {}
    run = {}
    run[args.getSampleID()] = parseQDM(args.getInput())
    runs[args.getRunID()] = run

    print(runs)
    return 0

if __name__ == "__main__":
    sys.exit(main())

