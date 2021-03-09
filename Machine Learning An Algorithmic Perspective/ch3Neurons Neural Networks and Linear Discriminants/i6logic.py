from numpy import *
inputs = array([[0,0],[0,1],[1,0],[1,1]])
# AND data
ANDtargets = array([[0],[0],[0],[1]])
# OR data
ORtargets = array([[0],[1],[1],[1]])
# XOR data
XORtargets = array([[0],[1],[1],[0]])
import pcn_logic_eg

print( "AND logic function")
p = pcn_logic_eg.pcn(inputs,ANDtargets)
p.pcntrain(inputs,ANDtargets,0.25,6)

print( "OR logic function")
p = pcn_logic_eg.pcn(inputs,ORtargets)
p.pcntrain(inputs,ORtargets,0.25,6)

print( "XOR logic function")
p = pcn_logic_eg.pcn(inputs,XORtargets)
p.pcntrain(inputs,XORtargets,0.25,6)