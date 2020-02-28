from typing import List, AnyStr
import csv
import sys

class IncompatibleRowException(Exception):
    """Error to throw when rows are incompatible"""
    def __init__(self, message):
        self.message = message


class SummaryTable:
    """Class that represents a summary table"""
    def __init__(self, headerRow: List):
        self.headerLength = len(headerRow)
        self.matrix = [headerRow]
    
    def getHeader(self):
        return ", ".join(self.matrix[0])
    
    def addRow(self, row: List):
        if len(row) != self.headerLength:
            raise IncompatibleRowException(f'Length of row not { self.headerLength }')
        else:
            self.matrix.append(row)
    
    def toCSV(self, output: AnyStr):
        with open(output, 'w', newline='') as file:
            csv.writer(file).writerows(self.matrix)
            
    
                
            
    
        
with open('data/SummaryTable.csv') as csvFile:
    SummaryTableReader = csv.reader(csvFile, delimiter=",")
    for row in SummaryTableReader:
        joint_row = ", ".join(row)
        if len(row) == 0 or joint_row.startswith('#') or (joint_row.startswith("Extracted") or joint_row.startswith("Called") or joint_row.startswith("Scored")):
            continue
        elif len(row) == 1:
            try:
                currentTable.toCSV(f'{currentTableID}.csv')
            except NameError:
                pass
            currentTableID = joint_row
            lineCount = 0
        elif len(row) > 1 and lineCount == 0:
            currentTable = SummaryTable(row)
            lineCount += 1
        else:
            try:
                currentTable.addRow(row)
            except IncompatibleRowException:
                print(f'Something went wrong while parsing the table {currentTableID}')
                print(f'Header: {currentTable.getHeader()} incompatible with: {joint_row}')
                sys.exit("Quitting Program due to parsing error")


