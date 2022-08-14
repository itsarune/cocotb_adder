COCOTB_HDL_TIMEUNIT ?= 1ns
COCOTB_HDL_TIMEPRECISION ?= 1ns

VERILOG_SOURCES ?= adder.sv
TOPLEVEL := adder
MODULE ?= tb_top

include $(shell cocotb-config --makefiles)/Makefile.sim
