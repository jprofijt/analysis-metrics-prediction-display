#! /usr/bin/env python2
import xml.etree.ElementTree as ET
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
    

print parseRun("data/interop/171130_NB501093_0223_AHVHNNAFXX/Info/RunInfo.xml").toDatabaseEntry()