#! /usr/bin/env python3

import csv, os, argparse, sys


class Files:
    """
    Class that contains input and output file locations
    """
    input = ''
    output = ''

    def getInput(self):
        """
        gets input file location

        :returns: input file path
        :rtype: str
        """
        return self.input
    
    def getOutput(self):
        """
        gets output file location

        :returns: output file path
        :rtype: str
        """
        return self.output

def getItem(row, columnID):
    """
    Tries to get the item from column, If that fails enter NA

    :param row: dict with items in a row
    :param columnID: Column to parse from row
    :returns: item parsed from row
    :rtype: str
    """
    try:
        item = row[columnID]
        if len(item) == 0:
            item = 'NA'
    except KeyError:
        item = 'NA'
    return item

def appendToFile(newRow, file):
    """
    Adds a row of items to the file

    :param newRow: list of items to add in order
    :param file: file path
    :rtype: void
    """
    with open(file,'a') as csvfile:
        csv.writer(csvfile).writerow(newRow)

def createFile(file, header = ['externalSampleID', 'Gender', 'sequencingStartDate', 'sequencer', 'prepKit', 'capturingKit', 'project']):
    """
    creates a new output file if it doesn't exist

    :param file: file path
    :param header: header to use for file, list of header names
    :rtype void
    """
    if not os.path.isfile(file):
        with open(file, 'w', newline='') as newCsv:
            writer = csv.writer(newCsv)
            writer.writerow(header)
    
def parseSampleSheet(infile, outfile, columns = ['externalSampleID', 'Gender', 'sequencingStartDate', 'sequencer', 'prepKit', 'capturingKit', 'project']):
    """
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
    """
    Uses argparse to parse input and output file from commandline
    
    :returns: file locations
    :rtype: class Files
    """
    parser = argparse.ArgumentParser(description='Parses sample sheet and adds to output file')
    parser.add_argument('-i', '--input', type=str, help='Sample sheet to read')
    parser.add_argument('-o', '--output', type=str, help='file to add results to')
    files = Files()
    parser.parse_args(namespace=files)
    return files

def main():
    """
    Main function, calls argparser, then checks output file by calling createFile, and finally proccesses Sample sheet

    :returns: exit code
    :rtype: int
    """
    fileContainer = parseArguments()

    createFile(fileContainer.getOutput())
    parseSampleSheet(fileContainer.getInput(), fileContainer.getOutput())

    return 0

if __name__ == "__main__":
    sys.exit(main())
    

