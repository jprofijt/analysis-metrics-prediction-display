
import csv
import sys


class IncompatibleRowException(Exception):
    """Error to throw when rows are incompatible"""
    def __init__(self, message):
        self.message = message


class SummaryTable:
    """Class that represents a summary table"""
    def __init__(self, headerRow):
        self.headerLength = len(headerRow)
        self.matrix = [headerRow]

    def getHeader(self):
        return ", ".join(self.matrix[0])

    def addRow(self, row):
        if len(row) != self.headerLength:
            raise \
                IncompatibleRowException(
                    "Length of row not {0}".format(self.headerLength)
                    )
        else:
            self.matrix.append(row)

    def toCSV(self, output):
        with open(output, 'w', newline='') as file:
            csv.writer(file).writerows(self.matrix)

def main():
    with open('data/SummaryTable.csv') as csvFile:
        SummaryTableReader = csv.reader(csvFile, delimiter=",")
        lineCount = 0
        for row in SummaryTableReader:
            joint_row = ", ".join(row)
            lineAtStartorEnd = (
                joint_row.startswith('#')
                or joint_row.startswith("Extracted")
                or joint_row.startswith("Called")
                or joint_row.startswith("Scored")
                )

            if len(row) == 0 or lineAtStartorEnd:
                continue

            elif len(row) == 1:
                try:
                    currentTable.toCSV("{0}.csv".format(currentTableID))
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
                    print(
                        """
                        Something went wrong while parsing the table {0}
                        Header: {1} incompatible with: {2}
                        """.format(
                            currentTableID,
                            currentTable.getHeader(),
                            joint_row
                        ))

                    return 1
        return 0

if __name__ == "__main__":
    main()
