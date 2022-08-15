import cocotb
from uvm import *

class RandomAdderTest(UVMTest) :
	def __init__(self, name="Random Adder Test", parent=None) :
		super().__init__(name, parent)
        self.test_pass = True
        self.tb0 = None
        self.printer = None

    async def run_phase(phase):
        phase.raise_objection(self, "random adder test objection raised")
        sqr = self.adder_tb.m_env.adder_agent.sequencer

        uvm_info("RANDOM ADDER TEST", "forking master proc seq", UVM_LOW)
        seq = sequence()
        proc = cocotb.fork(seq.start(sqr))
	    
        await sv.fork.join_any([proc])	
        phase.drop_objection(self, "random adder test objection dropped")

uvm_component_utils(RandomAdderTest)	


