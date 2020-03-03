#! /usr/bin/env python2.6

from __future__ import with_statement
from __future__ import absolute_import
import csv, os, argparse, sys
from io import open


class Files(object):
    u"""
    Class that contains input and output file locations
    """
    def __init__(self, input, output):
        self.input = input
        self.output = output

    def getInput(self):
        u"""
        gets input file location

        :returns: input file path
        :rtype: str
        """
        return self.input
    
    def getOutput(self):
        u"""
        gets output file location

        :returns: output file path
        :rtype: str
        """
        return self.output

def getItem(row, columnID):
    u"""
    Tries to get the item from column, If that fails enter NA

    :param row: dict with items in a row
    :param columnID: Column to parse from row
    :returns: item parsed from row
    :rtype: str
    """
    try:
        item = row[columnID]
        if len(item) == 0:
            item = u'NA'
    except KeyError:
        item = u'NA'
    return item

def appendToFile(newRow, file):
    u"""
    Adds a row of items to the file

    :param newRow: list of items to add in order
    :param file: file path
    :rtype: void
    """
    with open(file,'ab') as csvfile:
        csv.writer(csvfile).writerow(newRow)

def createFile(file, header = ['externalSampleID', 'Gender', 'sequencingStartDate', 'sequencer', 'prepKit', 'capturingKit', 'project']):
    u"""
    creates a new output file if it doesn't exist

    :param file: file path
    :param header: header to use for file, list of header names
    :rtype void
    """
    if not os.path.isfile(file):
        with open(file, 'wb') as newCsv:
            writer = csv.writer(newCsv, delimiter=',', quotechar='#', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(header)
    
def parseSampleSheet(infile, outfile, columns = ['externalSampleID', 'Gender', 'sequencingStartDate', 'sequencer', 'prepKit', 'capturingKit', 'project']):
    u"""
    moves wanted columns from samplesheet to output csv

    :param infile: input sample sheet csv
    :param outfile: output sample sheet csv
    :param columns: columns to parse, list of column names
    :rtype: void
    """
    with open(infile, mode='r') as sampleSheet:
            reader = csv.DictReader(sampleSheet, delimiter=",") 
            for row in reader:
                appendToFile([getItem(row, column) for column in columns], outfile)

def parseArguments():
    u"""
    Uses argparse to parse input and output file from commandline
    
    :returns: file locations
    :rtype: class Files
    """
    parser = argparse.ArgumentParser(description=u'Parses sample sheet and adds to output file')
    parser.add_argument(u'-i', u'--input', type=unicode, help=u'Sample sheet to read')
    parser.add_argument(u'-o', u'--output', type=unicode, help=u'file to add results to')
    args = parser.parse_args()
    files = Files(args.input, args.output)
    return files

def main():
    u"""
    Main function, calls argparser, then checks output file by calling createFile, and finally proccesses Sample sheet

    :returns: exit code
    :rtype: int
    """
    fileContainer = parseArguments()

    createFile(fileContainer.getOutput())
    parseSampleSheet(fileContainer.getInput(), fileContainer.getOutput())

    return 0

if __name__ == u"__main__":
    sys.exit(main())
    

