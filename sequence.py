from uvm.seq import UVMSequence, UVMSequencer
from uvm.macros import uvm_object_utils, uvm_do_on
from trans import trans
from uvm import *
from cocotb.triggers import Timer

class sequence(UVMSequence):
    def __init__(self, name="adder sequence"):
        UVMSequence.__init__(self, name)
        self.sqr = None
        self.req = None
        self.rsp = None

    def build_phase(self, phase):
        UVMEnv.build_phase(self, phase)
        #self.sqr = UVMSequence.__init__(self, name="test seqr")
    
    async def body(self):
        if (self.sqr is None) :
           Exception("Null sequencer!") 
        print("SEQ, seqr " + str(self.sqr))
        for i in range(0, 10) :
            self.req = trans()
            self.req.randomize()
            
            await self.start_item(item=self.req, sequencer=self.sqr)
            await self.finish_item(self.req)

            rsp = []
            await self.get_response(rsp)
            self.rsp = rsp[0]

            uvm_info(self.get_name(), sv.sformatf("input1: %d, input2: %d", self.req.input1, self.req.input2), UVM_LOW)
            await Timer(5, "NS")

uvm_object_utils(sequence)
