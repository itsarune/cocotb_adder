from uvm.comps import UVMEnv
from uvm.macros import uvm_component_utils
from monitor import monitor
from uvm.base.uvm_config_db import UVMConfigDb
from agent import agent
from uvm import *

class env(UVMEnv) :
    def __init__(self, name, parent) :
        UVMEnv.__init__(self, name, parent)
        self.monitor = None
        self.vif = None
        self.adder_agent = None
        uvm_info("env", "env created!", UVM_FULL)

    def build_phase(self, phase) :
        inst_name = "env"
        super().build_phase(phase)
        
        arr = []
        if UVMConfigDb.get(None, "*", "vif", arr) is False:
            uvm_fatal(self.get_name(), "no VIF found!")
        self.vif = arr[0]

        self.monitor = monitor.type_id.create("monitor", self)
        self.adder_agent = agent.type_id.create("adder agent", self)


uvm_component_utils(env)
