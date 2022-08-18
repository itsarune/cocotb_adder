from uvm.seq import UVMSequenceItem
from uvm.macros import * 
from trans import trans
from uvm.base.uvm_object_globals import UVM_ALL_ON

class adder_item(UVMSequenceItem) :
	def __init__(self, name="adder_item"):
		UVMSequenceItem.__init__(self, name)
		self.input1 = 0
		self.input2 = 0
		self.answer = 0

uvm_object_utils_begin(trans)
uvm_field_int('input1', UVM_ALL_ON)
uvm_field_int('input2', UVM_ALL_ON)
uvm_field_int('answer',UVM_ALL_ON)
uvm_field_utils_end(trans)
