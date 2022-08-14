from uvm.seq import UVMSequencer

class sequencer(UVMSequencer) :
	def __init__(self, name, parent) :
		UVMSequencer.__init__(self, name, parent)

uvm_component_utils(sequencer)
