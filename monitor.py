from uvm.comps import UVMDriver
from cocotb.triggers import Edge

class Monitor(UVMMonitor) :
	def __init__(self, name, parent=None) :
		UVMMonitor.__init__(self, name, parent)
		self.vif = None
		self.item_collected_port = UVMAnalysisPort("item_collected_port", self)
		self.collected_item = adder_item()

	def build_phase(self, phase) :
		arr = []
		if UVMConfigDb.get(self, "", "vif", arr) :
			self.vif = arr[0]
		if self.vif is None :
			uvm_report_fatal("NOVIF", "no virtual interface found in config db")

	def run_phase(self, phase) :
		await Timer(0, "ns")
		while True :
			await Edge(self.vif.A)	
			self.collected_item.answer <= self.vif.X
			uvm_info("UVMMonitor", sv.sformatf("item: %s\n", self.collected_item.sprint()), UVM_LOW)
			self.item_collected_port.write(self.collected_item)
		
