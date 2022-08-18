from uvm.macros import uvm_component_utils
from uvm.comps import UVMScoreboard
from uvm.tlm1 import UVMAnalysisImp
from uvm import uvm_info
from uvm import *
from trans import trans

class scoreboard(UVMScoreboard) :
	def __init__(self, name, parent) :
		UVMScoreboard.__init__(self, name, parent)
		self.disable_scoreboard = False	
		self.item_collected_export = None

	def build_phase(self, phase) :
		self.item_collected_export = UVMAnalysisImp("item_collected_export", self)

	def write(self, trans) :
		uvm_info(self.get_type_name(), sv.sformatf("transans: %d, %d, %d", trans.input1, trans.input2, trans.answer), UVM_LOW)

		if (int(trans.answer) != (int(trans.input1) + int(trans.input2))) :
			uvm_error(self.get_type_name(), sv.sformatf("adder mismatch. Expected (modelling): %h, Actual (dut): %h", int(trans.input1)+int(trans.input2), int(trans.answer)))

uvm_component_utils(scoreboard)
	
