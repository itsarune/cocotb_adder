import cocotb

from uvm.base.sv import sv_if, sv
from cocotb.triggers import Combine, Edge

class adder_if(sv_if) :
    def __init__(self, dut) :
        bus_map = {
            "A": "A", "B": "B", "X": "X" }
        sv_if.__init__(self, dut, "", bus_map)
        self.has_checks = True
        self.has_coverage = True

    async def start(self):
        a = cocotb.fork(self.drive_data())
        await sv.fork_join([a])
    
    # TODO: Review later, I don't think this is necessary
    async def drive_data(self) :
        while True :
            await Combine(Edge(self.A), Edge(self.B))
            self.A <= self.A.value
            self.B <= self.B.value
