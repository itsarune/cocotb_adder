from uvm.comps import UVMEnv
from uvm import *
from uvm.macros import uvm_component_utils
from env import env
from scoreboard import scoreboard

import cocotb

class adder_tb(UVMEnv) :
    def __init__(self, name, parent=None) :
        UVMEnv.__init__(self, name, parent)
        self.scoreboard = None
        self.m_env = None
        uvm_info("adder_tb", "adder_tb created", UVM_LOW)

    def build_phase(self, phase) :
        self.m_env = env.type_id.create("m_env", self)
        self.scoreboard = scoreboard.type_id.create("scoreboard", self)

    def connect_phase(self, phase) :
        self.m_env.monitor.item_collected_port.connect(self.scoreboard.item_collected_export)

uvm_component_utils(adder_tb)
