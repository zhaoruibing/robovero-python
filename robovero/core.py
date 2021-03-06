"""Core library functions. See LPC17xx CMSIS-Compliant Standard Peripheral
Firmware Driver Library documentation.
"""

from internals import RoboCaller

__author__ =			"Neil MacMunn"
__email__ =				"neil@gumstix.com"
__copyright__ = 	"Copyright 2010, Gumstix Inc."
__license__ = 		"BSD 2-Clause"
__version__ =			"0.1"


def NVIC_EnableIRQ(IRQn):
	"""Enable an interrupt.
	
	Args:
	
	- IRQn(IRQn_Type): class IRQn_Type from LPC17XX.py
	
	"""
	return RoboCaller().call("NVIC_EnableIRQ", "void", IRQn)

def NVIC_ClearPendingIRQ(IRQn):
	"""Clear a pending interrupt.
	
	Args:

	- IRQn(IRQn_Type): class IRQn_Type from LPC17XX.py
	
	Note that this is automatically done for you after your ISR is called,
	before 

	"""
	return RoboCaller().call("NVIC_ClearPendingIRQ", "void", IRQn)
