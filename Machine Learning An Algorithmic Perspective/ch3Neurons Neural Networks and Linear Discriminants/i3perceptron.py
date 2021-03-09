from numpy import *
import pcn_logic_eg

inputs = array([ [0,0],[0,1],[1,0],[1,1]  ])
print('inputs=\n',inputs)

targets = array([ [0],[1],[1],[1] ])
print('targets=\n',targets)


p = pcn_logic_eg.pcn(inputs, targets)
p.pcntrain(inputs, targets, 0.25, 6)