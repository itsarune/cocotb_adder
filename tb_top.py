from adder_if import adder_if

import cocotb

async def initial_run_test(dut, vif):
    from uvm.base import UVMCoreService
    cs_ = UVMCoreService.get()
    UVMConfigDb.set(None, "*", "vif", vif)
    await run_test()

@cocotb.test()
async def module_tb(dut) :

    vif = adder_if(dut)

    proc_run_test = cocotb.fork(initial_run_test(dut, vif))
    proc_vif = cocotb.fork(vif.start())

    await sv.fork_join([proc_run_test])
