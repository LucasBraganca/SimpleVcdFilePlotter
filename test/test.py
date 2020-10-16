import os
import sys

mypath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.vcd_parser import VcdParser

vcd_parser = VcdParser()
ss = vcd_parser.parse(mypath+'/out.vcd')

for s in ss.signals:
    print(ss.signals[s])
    print(ss.signals[s].getValues(ss.getMaxTimeStamp()))
    print()
