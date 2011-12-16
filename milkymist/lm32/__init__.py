from migen.fhdl import structure as f
from migen.bus import wishbone

class Inst:
	def __init__(self):
		self.ibus = i = wishbone.Master("lm32i")
		self.dbus = d = wishbone.Master("lm32d")
		f.declare_signal(self, "interrupt", f.BV(32))
		f.declare_signal(self, "ext_break")
		self._inst = f.Instance("lm32_top",
			[("I_ADR_O", i.adr_o),
			("I_DAT_O", i.dat_o),
			("I_SEL_O", i.sel_o),
			("I_CYC_O", i.cyc_o),
			("I_STB_O", i.stb_o),
			("I_WE_O", i.we_o),
			("I_CTI_O", i.cti_o),
			("I_LOCK_O", f.BV(1)),
			("I_BTE_O", i.bte_o),
			("D_ADR_O", d.adr_o),
			("D_DAT_O", d.dat_o),
			("D_SEL_O", d.sel_o),
			("D_CYC_O", d.cyc_o),
			("D_STB_O", d.stb_o),
			("D_WE_O", d.we_o),
			("D_CTI_O", d.cti_o),
			("D_LOCK_O", f.BV(1)),
			("D_BTE_O", d.bte_o)],
			[("interrupt", self.interrupt),
			#("ext_break", self.ext_break),
			("I_DAT_I", i.dat_i),
			("I_ACK_I", i.ack_i),
			("I_ERR_I", i.err_i),
			("I_RTY_I", f.BV(1)),
			("D_DAT_I", d.dat_i),
			("D_ACK_I", d.ack_i),
			("D_ERR_I", d.err_i),
			("D_RTY_I", f.BV(1))],
			[],
			"clk_i",
			"rst_i",
			"lm32")

	def get_fragment(self):
		comb = [
			f.Assign(self._inst.ins["I_RTY_I"], 0),
			f.Assign(self._inst.ins["D_RTY_I"], 0)
		]
		return f.Fragment(comb=comb, instances=[self._inst])