from uvm.comps import UVMAgent

class agent(UVMAgent) :
	def __init__(self, name, parent) :
		self.driver = None
		self.monitor = None
		self.sequencer = None

	def build_phase(self, phase) :
		super().build_phase(phase)
		self.monitor = monitor.type_id.create("monitor", self)
		if self.get_is_active() == UVM_ACTIVE :
			self.driver = driver.type_id.create("driver", self)
			self.sequencer = sequence.type_id.create("sequencer", self)
	
	def connect_phase(self, phase) :
		if self.get_is_active() == UVM_ACTIVE :
			self.driver.seq_item_port.connect(self.sequencer.seq_item_export)

uvm_component_utils(agent)
