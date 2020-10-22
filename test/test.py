import os
import sys

mypath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.vcd_plotter import VcdPlotter

vcd_plt = VcdPlotter(mypath+'/out.vcd')

vcd_plt.print_signals()
vcd_plt.show(['tb.clk','tb.vadd.a','tb.x'],0,50,'bin')
vcd_plt.save_figure('out.pdf',['tb.clk','tb.vadd.a','tb.x'],0,400,'bin')
