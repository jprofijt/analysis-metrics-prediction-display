import xml.etree.ElementTree as ET

tree = ET.parse("data/interop/171130_NB501093_0223_AHVHNNAFXX/Info/RunInfo.xml")

root = tree.getroot()


run = root.find("Run")
number = root.get("Number")
FlowCell = run.find("Flowcell")
Sequencer = run.find("Instrument")
Date = run.find("Date")

print run.attrib, FlowCell.text, Sequencer.text, Date.text