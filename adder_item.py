class adder_item(UVMSequenceItem) :
	def __init__(self, name="adder_item"):
		self.input1 = 0
		self.input2 = 0
		self.answer = 0

uvm_object_utils(adder_item)	
