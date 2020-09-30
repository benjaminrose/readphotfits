"""savephotfits.py - covert SNANA fits to a human readable format.

An example of how to use readphotfits.py.

Authors: Ben Rose, Dillon Brout

Changelog:
 - 2020-09-29: Initial file creation.
 
 To do:
 - Change hardcoded example to a cli with defualts.
 """

import yaml
import json

import readphotfits

SCRATCH_SIMDIR = '/scratch/midway2/rkessler/SNDATA_ROOT/SIM'
FOLDER1 = SCRATCH_SIMDIR + '/Deep_Spec_BR_Yeswiggle'
FOLDER2 = SCRATCH_SIMDIR + '/Deep_Spec_BR_Nowiggle'

result1 = readphotfits.getphotdict(FOLDER1, 5)
result2 = readphotfits.getphotdict(FOLDER2, 5)

#breakpoint()    # uncomment to use pdb/debug as an interactive env

with open('yeswiggle.txt', 'w') as f:
    print(str(result1), file=f)
with open('nowiggle.txt', 'w') as f:
    print(str(result2), file=f)

