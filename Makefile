COCOTB_HDL_TIMEUNIT ?= 1ns
COCOTB_HDL_TIMEPRECISION ?= 1ns

VERILOG_SOURCES ?= adder.sv
TOPLEVEL := adder
MODULE ?= test_adder

include $(shell cocotb-config --makefiles)/Makefile.sim
