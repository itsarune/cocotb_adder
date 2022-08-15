from uvm.seq import UVMSequenceItem
from cocotb.binary import BinaryValue

class trans(UVMSequenceItem, crv.Randomized) :
	def __init__(self, name="adder trans item") :
		UVMSequenceItem.__init__(self, name)
		self.input1 = 0
		self.input2 = 0
		self.add_rand("input1", list(range(2**DATA_WIDTH)))
        self.add_rand("input2", list(range(2**DATA_WIDTH)))

	uvm_object_utils_begin(bus_trans)
	uvm_field_int('input1', UVM_ALL_ON)
	uvm_field_int('input2', UVM_ALL_ON)
	uvm_field_utils_end(bus_trans)

class bus_rsp(trans) :
	def __init__(self, name="bus rsp") :
		trans.__init__(self, name)
		self.status = 0

class bus_req(trans) :
	def __init__(self, name="bus req") :
		trans.__init__(self, name)
uvm_object_util(bus_req)
