from uvm import *
from testbench import adder_tb
from env import env
from sequence import sequence
from uvm.base.sv import sv

import cocotb

class test_adder_random(UVMTest) :
    def __init__(self, name="Random Adder Test", parent=None) :
        super().__init__(name, parent)
        self.test_pass = True
        self.tb0 = None
        self.printer = None

    def build_phase(self, phase):
        super().build_phase(phase)
        UVMConfigDb.set(self, "*", "recording_detail", UVM_LOW)
        self.tb0 = adder_tb.type_id.create("tb0", self)
        self.printer = UVMTablePrinter()
        self.printer.knobs.depth = 3

        arr = []
        if UVMConfigDb.get(None, "*", "vif", arr) is True :
            UVMConfigDb.set(self, "*", "vif", arr[0])
        else :
            uvm_fatal("RAT", "no VIF found in the config DB")

    async def run_phase(self, phase):
        phase.raise_objection(self, "random adder test objection raised")
        sqr = self.tb0.m_env.adder_agent.sequencer

        print("RAT " + str(sqr))

        uvm_info("RANDOM ADDER TEST", "forking master proc seq", UVM_LOW)
        seq = sequence.type_id.create("seq", self)
        seq.sqr = sqr
        proc = cocotb.fork(seq.start(sqr))
        
        await sv.fork_join_any([proc])  
        phase.drop_objection(self, "random adder test objection dropped")

uvm_component_utils(test_adder_random)  


