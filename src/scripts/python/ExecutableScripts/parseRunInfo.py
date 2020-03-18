#! /usr/bin/env python2
import xml.etree.ElementTree as ET
import subprocess
from QualityParser.DataTypes import SequencingRun
from QualityParser.Parsers import dateParserz

def parseRun(xml):
    tree = ET.parse(xml)

    root = tree.getroot()


    run = root.find("Run")
    number = root.get("Number")
    FlowCell = run.find("Flowcell")
    Sequencer = run.find("Instrument")
    Date = run.find("Date")
    
    return SequencingRun(run.attrib["Id"], run.attrib["Number"], FlowCell.text, Sequencer.text, dateParser(Date.text.strip()))
    
def dumpInterop(interop, application):
    dumptext = subprocess.check_output([application, interop])

