class scoreboard(UVMScoreboard) :
	def __init__(self, name, parent) :
		self.disable_scoreboard = False	

	def build_phase(self, phase) :
		self.item_collected_export = UVMAnalysisImp("item_collected_export", self)

	def write(self, trans) :
		uvm_info(self.get_type_name(), sv.sformatf("trans input1: %h, input2: %h, adder answer: %h", trans.input1, trans.input2, trans.answer), UVM_LOW)
		if (!trans.answer == (trans.input1 + trans.input2)) :
			uvm_error(self.get_type_name(), sv.sofrmatf("adder mismatch. Expected (modelling): %h, Actual (dut): %h", trans.input+trans.input2, trans.answer))

uvm_component_utils(scoreboard)
	
