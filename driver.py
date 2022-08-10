from uvm.comps import UVMDriver

class driver(UVMDriver) :
	def __init__(self, name="adder driver", parent) :
		UVMDriver.__init__(self, name, parent)
		self.vif = None
	
	def build_phase(self, phase) :
		super().build_phase(self, phase)
		arr = []
		if UVMConfigDb.get(self, "", "vif", arr)
			self.vif = arr[0]
		if self.vif is None :
			self.uvm_report_fatal("NOVIF", "no virtual interface in config db!")	
		
	async def run_phase(self, phase) :	
		req = None
		rsp = None

		while True :
			uvm_info("arun", "driver getting request", UVM_LOW)
			qreq = []
			await self.seq_item_port.get(qreq)
			
			self.nitems += 1
			req = qreq[0]

			rsp = req.clone()
			rsp.set_id_info(req[0])

			await self.drive_transfer(rsp)

			self.seq_item_port.item_dome()
			self.seq_item_port.put_response(rsp)
	
	async def drive_transfer(self, trans) :	
		vif.A <= trans.input1
		vif.B <= trans.input2


uvm_component_utils(driver)
