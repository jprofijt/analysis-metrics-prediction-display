import csv, os, argparse, sys


class Files:
    input = ''
    output = ''

    def getInput(self):
        return self.input
    
    def getOutput(self):
        return self.output

def getItem(row, columnID):
    """
    Tries to get the item from column, If that fails enter NA
    @row dict with row items
    @columnID column to parse from row
    """
    try:
        item = row[columnID]
        if len(item) == 0:
            item = 'NA'
    except KeyError:
        item = 'NA'
    return item

def appendToFile(newRow, file):
    print(newRow)
    with open(file,'a') as csvfile:
        csv.writer(csvfile).writerow(newRow)

def createFile(file, header = ['externalSampleID', 'Gender', 'sequencingStartDate', 'sequencer', 'prepKit', 'capturingKit', 'project']):
    if not os.path.isfile(file):
        with open(file, 'w', newline='') as newCsv:
            writer = csv.writer(newCsv)
            writer.writerow(header)
    
def parseSampleSheet(infile, outfile, columns = ['externalSampleID', 'Gender', 'sequencingStartDate', 'sequencer', 'prepKit', 'capturingKit', 'project']):
    with open(infile, mode='r') as sampleSheet:
            reader = csv.DictReader(sampleSheet, delimiter=",") 
            for row in reader:
                
                appendToFile([getItem(row, column) for column in columns], outfile)

def parseArguments():
    parser = argparse.ArgumentParser(description='Parses sample sheet and adds to output file')
    parser.add_argument('-i', '--input', type=str, help='Sample sheet to read')
    parser.add_argument('-o', '--output', type=str, help='file to add results to')
    files = Files()
    parser.parse_args(namespace=files)
    return files

def main():
    fileContainer = parseArguments()

    createFile(fileContainer.getOutput())
    parseSampleSheet(fileContainer.getInput(), fileContainer.getOutput())

    return 0

if __name__ == "__main__":
    sys.exit(main())
    

