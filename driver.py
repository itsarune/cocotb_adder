from uvm.comps import UVMDriver
from uvm.base import UVMConfigDb
from uvm.macros import uvm_component_utils

from uvm import *

class driver(UVMDriver) :
    def __init__(self, name="adder driver", parent=None) :
        UVMDriver.__init__(self, name, parent)
        self.vif = None
        self.nitems = 0
    
    def build_phase(self, phase) :
        super().build_phase(phase)
        arr = []
        if UVMConfigDb.get(self, "", "vif", arr) :
            self.vif = arr[0]
        if self.vif is None :
            self.uvm_report_fatal("NOVIF", "no virtual interface in config db!")    
        
    async def run_phase(self, phase) :  
        req = None
        rsp = None

        while True :
            uvm_info("arun", "driver getting request", UVM_LOW)
            qreq = []
            await self.seq_item_port.get_next_item(qreq)
            uvm_info("arun", sv.sformatf("got item from seq item port: a:%d, b:%d", qreq[0].input1, qreq[0].input2), UVM_LOW)  

            self.nitems += 1
            req = qreq[0]

            rsp = req.clone()
            rsp.set_id_info(req)

            await self.drive_transfer(rsp)

            self.seq_item_port.item_done()
            self.seq_item_port.put_response(rsp)
    
    async def drive_transfer(self, trans) : 
        self.vif.a <= trans.input1
        self.vif.b <= trans.input2


uvm_component_utils(driver)
