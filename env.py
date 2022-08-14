from uvm.comps import UVMEnv

class env(UVMEnv) :
	def __init__(name, parent) :
		self.monitor = None
		self.vif = None

	def build_phase(self, phase) :
		inst_name = "env"
		super().build_phase(phase)
		
		arr = []
		if !UVMConfigDb.get(None, "*", "vif", arr) :
			uvm_fatal(self.get_name(), "no VIF found!")
		self.vif = arr[0]

		self.monitor = monitor.type_id.create("monitor", self)


uvm_component_utils(env)
