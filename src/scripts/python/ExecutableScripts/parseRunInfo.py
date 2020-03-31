#! /usr/bin/env python2
import xml.etree.ElementTree as ET
import subprocess
from QualityParser.DataTypes import SequencingRun
from QualityParser.Parsers import dateParser

def parseRun(xml):
    tree = ET.parse(xml)

    root = tree.getroot()


    run = root.find("Run")
    number = root.get("Number")
    FlowCell = run.find("Flowcell")
    Sequencer = run.find("Instrument")
    Date = run.find("Date")
    
    return SequencingRun(run.attrib["Id"], run.attrib["Number"], FlowCell.text, Sequencer.text, dateParser(Date.text.strip()))
    
def getInteropSummary(interop, summaryApplication):
    summary = subprocess.check_output([summaryApplication, interop, '--level=0', '--csv=1'])
    return summary.strip().split("\n")[2:4]

