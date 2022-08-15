class sequence(UVMSequence):
    def __init__(self, name="adder sequence"):
        UVMSequence.__init__(self, name)
        self.trans = trans()

    async def body(self):
        trans.randomize()
        await uvm_do(trans)

        rsp = []
        await self.get_response(req)
        self.rsp = rsp[0]

        uvm_info(self.get_name(), sv.sformatf("input1: %d, input2: %d", self.rsp.input1, self.rsp.input2), UVM_HIGH)

uvm_object_utils(sequence)
