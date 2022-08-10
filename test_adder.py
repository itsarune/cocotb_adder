import cocotb
from uvm import *

class RandomAdderTest(UVMTest) :
	def __init__(self, name="Random Adder Test", parent=None) :
		super().__init__(name, parent)
		

uvm_component_utils(RandomAdderTest)	


