#!/usr/bin/env python
"""Test a batch of files, assure that they are parsed successfully
and have the correct type of information stored
"""

import sys
import os
import unittest
import datetime
import itertools
pathToThisFile = os.path.realpath(__file__)
try:
    import parseCmmMeas
except:
    # wasn't able to import parseCmmMeas (was not found on environment variable PYTHONPATH)
    # the following lines are required to make python "see" this package
    # so import parseCmmMeas works
    # find the path to base directory of this package
    pathToBase, discardMe = pathToThisFile.split("/tests/")
    sys.path.append(pathToBase + "/python")
    # python should now see this package
    import parseCmmMeas