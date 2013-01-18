#!env python
__author__ = 'bryukh'
import unittest
import all_settings

from base_tests import SvgTest, suite

PATHS = ['icons_tasks/',] #, 'badges/', 'icons_interface/']

class IconTaskTest(SvgTest):
    pass

if __name__ == '__main__':
    settings = {
                    'size': all_settings.ICONS_TASKS_SIZE,
                    'colors': all_settings.COLORS
                }
    unittest.TextTestRunner(verbosity=2).run(suite(IconTaskTest, PATHS, settings))