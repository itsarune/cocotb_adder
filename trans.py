from uvm.seq import UVMSequenceItem
from cocotb.binary import BinaryValue
from cocotb_coverage import *
from uvm.macros import * 
from uvm.base.uvm_object_globals import UVM_ALL_ON
from common import DATA_WIDTH

class trans(UVMSequenceItem, crv.Randomized) :
    def __init__(self, name="adder trans item") :
        UVMSequenceItem.__init__(self, name)
        self.input1 = 0
        self.input2 = 0
        self.answer = 0
        self.add_rand("input1", list(range(2**DATA_WIDTH)))
        self.add_rand("input2", list(range(2**DATA_WIDTH)))

uvm_object_utils_begin(trans)
uvm_field_int('input1', UVM_ALL_ON)
uvm_field_int('input2', UVM_ALL_ON)
uvm_field_utils_end(trans)

class bus_rsp(trans) :
    def __init__(self, name="bus rsp") :
        trans.__init__(self, name)
        self.status = 0

class bus_req(trans) :
    def __init__(self, name="bus req") :
        trans.__init__(self, name)

uvm_object_utils(bus_req)
