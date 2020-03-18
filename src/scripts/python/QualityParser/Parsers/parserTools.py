#! /usr/bin/env python2.7

import argparse
from ..DataTypes.Files import Files
import datetime
def decomment(csvfile):
    for row in csvfile:
        raw = row.split(u'#')[0].strip()
        if raw: yield raw

def inputOutputParser():

    # Python 2, disable unicode error
    # pylint: disable=undefined-variable
    u"""
    Uses argparse to parse input and output file from commandline
    
    :returns: file locations
    :rtype: class Files
    """
    parser = argparse.ArgumentParser(description=u'Parses sample sheet and adds to output file')
    parser.add_argument(u'-i', u'--input', type=unicode, metavar="path/to/input", help=u'Sample sheet to read', required=True)
    parser.add_argument(u'-o', u'--output', type=unicode, metavar="path/to/output", help=u'file to add results to', required=True)
    args = parser.parse_args()
    files = Files(args.input, args.output)
    return files

def createQuickParser(args, description):
    parser = argparse.ArgumentParser(description=description)
    for item in args:
        parser.add_argument(u"-{0}".format(item[0]), u"--{0}".format(item), type=unicode, required=True)
    
    return parser

def dateParser(dateString):
    return datetime.datetime.strptime(dateString, "%y%m%d").date()

