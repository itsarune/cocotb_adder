from uvm.comps import UVMAgent
from uvm.macros import uvm_component_utils
from uvm.base import UVMConfigDb
from sequencer import sequencer
from driver import driver
from monitor import monitor

from uvm import *

class agent(UVMAgent) :
    def __init__(self, name, parent) :
        super().__init__(name, parent)
        self.driver = None
        self.monitor = None
        self.sequencer = None
        uvm_info("AGE", "adder agent created", UVM_LOW)

    def build_phase(self, phase) :
        super().build_phase(phase)
        self.monitor = monitor.type_id.create("monitor", self)
        self.driver = driver.type_id.create("driver", self)
        self.sequencer = sequencer.type_id.create("sequencer", self)
        print("AGE ", str(self.sequencer))
    
    def connect_phase(self, phase) :
        self.driver.seq_item_port.connect(self.sequencer.seq_item_export)

uvm_component_utils(agent)
