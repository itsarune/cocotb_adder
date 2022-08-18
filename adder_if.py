import cocotb

from uvm.base.sv import sv_if, sv
from cocotb.triggers import Combine, Edge

class adder_if(sv_if) :
    def __init__(self, dut) :
        bus_map = {
            "a": "A", "b": "B", "x": "X" }
        sv_if.__init__(self, dut, "adder", bus_map)
        self.has_checks = True
        self.has_coverage = True
        self.answer = 0

    #async def start(self):
        #proc = cocotb.fork(self.drive_data())
        #wait sv.fork_join([proc])
        #void()
    
