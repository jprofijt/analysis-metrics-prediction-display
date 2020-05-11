#! /usr/bin/env python3
class RowLengthNotEqualToHeader(Exception):
    def __init__(self, headerLenght, rowLength, header, row, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Header: {0} columns, does not have not equal columns to Row: {1}.\n Header: {2}\n Row: {3}".format(headerLenght, rowLength, header, row))


class table(object):
    def __init__(self, header, name):
        self.name = name
        self.header = header
        self.columns = len(header)
        self.rows = []
    
    def addRow(self, row):
        rowlength = len(row)
        if self.columns == rowlength:
            self.rows.append(row)
        else:
            raise RowLengthNotEqualToHeader(self.columns, rowlength, self.header, row)
    
    def __str__(self):
        print(self.name)
        print(self.header)
        
        return "FI"

        
import fileinput
count = 0
nextline = False

for line in fileinput.input():
    count += 1
    if line.startswith("#"):
        if "Column Count:" in line:
            try:
                print(t)
                nextline = True
                continue
            except NameError:
                nextline = True
                continue
        else:
            continue
    elif nextline:
        t = table([x.strip() for x in line.split(",")], 'test')
        nextline = False
    else:
        try:
            t.addRow([x.strip() for x in line.split(",")])
        except RowLengthNotEqualToHeader:
            t.addRow([None] + [x.strip() for x in line.split(",")])
    