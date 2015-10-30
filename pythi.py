#!/usr/bin/env python3

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pyth'))
import pyth

import readline
import traceback

while True:
    try:
        exec(pyth.general_parse(input('>>> ')), pyth.environment)
    except EOFError:
        break
    except:
        traceback.print_exc()
