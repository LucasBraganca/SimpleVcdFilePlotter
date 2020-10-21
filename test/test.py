import os
import sys

mypath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.vcd_plotter import VcdPlotter

vcd_plt = VcdPlotter(mypath+'/out.vcd')

vcd_plt.save_figure('teste.pdf',['tb.clk','tb.vadd.a'],0,100,'bin')


