"""This sample script uses wsadminlib.py to display the WAS cell name."""
import yaml
execfile('wsadminlib.py')
cellName = getCellName()
print "cellName=" + cellName
