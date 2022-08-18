from uvm.seq import UVMSequencer
from uvm.macros import uvm_component_utils
from uvm import *

class sequencer(UVMSequencer) :
    def __init__(self, name, parent) :
        UVMSequencer.__init__(self, name, parent)
        uvm_info("SEQR", "sequencer created!", UVM_LOW)

uvm_component_utils(sequencer)
