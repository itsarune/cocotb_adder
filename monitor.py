from uvm.comps import UVMDriver, UVMMonitor
from cocotb.triggers import *
from uvm.macros import uvm_component_utils
from uvm.tlm1 import UVMAnalysisPort
from adder_item import adder_item
from uvm.base import * 
from uvm import uvm_info
from uvm.base.sv import sv

class monitor(UVMMonitor) :
    def __init__(self, name, parent=None) :
        UVMMonitor.__init__(self, name, parent)
        self.vif = None
        self.item_collected_port = UVMAnalysisPort("item_collected_port", self)
        self.collected_item = adder_item()

    def build_phase(self, phase) :
        arr = []
        if UVMConfigDb.get(self, "", "vif", arr) :
            self.vif = arr[0]
        if self.vif is None :
            uvm_report_fatal("NOVIF", "no virtual interface found in config db")

    async def run_phase(self, phase) :
        await Timer(0, "ns")
        while True :
            await Edge(self.vif.x)
            answer = int(self.vif.x)
            self.collected_item.answer = answer 
            self.collected_item.input1 = self.vif.a
            self.collected_item.input2 = self.vif.b
            uvm_info("UVMMonitor", sv.sformatf("item a:%h, b:%h\n", int(self.collected_item.input1), int(self.collected_item.input2)), UVM_LOW)
            uvm_info("UVMMonitor", sv.sformatf("item answer: %h", int(self.collected_item.answer)), UVM_LOW)
            self.item_collected_port.write(self.collected_item)
        
uvm_component_utils(monitor)
