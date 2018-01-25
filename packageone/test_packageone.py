#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 20:44:07 2018

@author: tanner
"""

import unittest

class TestPackageOne(unittest.TestCase):
    """ A TestCase (class) is used to group similar tests """

    def setUp(self):
        """ setUp gets called before each individual test method. """
        pass

    def tearDown(self):
        """ tearDown gets called after each individual test method. """
        pass

    def test_instantiation(self):
        """ Can we even instantiate this thing? """

        print('Test Instantiation')


#################################
### Module Level Test Harness ###
#################################
if __name__ == "__main__":

    # Kick off all unit tests contained in the file
    unittest.main(verbosity=2)