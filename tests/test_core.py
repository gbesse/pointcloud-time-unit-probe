import unittest,math
from pointcloud_time_unit_probe.core import run
class DomainTests(unittest.TestCase):
 def test_ambiguity_not_autoselect(self):
  x=run({'timestamps':[0,50000,100000],'scan_duration_seconds':.1});self.assertEqual(x['compatible_units'],['microseconds','nanoseconds']);self.assertFalse(x['unique'])
 def test_unique_nanoseconds(self):self.assertEqual(run({'timestamps':[0,100000000],'scan_duration_seconds':.1})['compatible_units'],['nanoseconds'])
 def test_absolute_origin(self):self.assertTrue(run({'timestamps':[1000000000,1000000001],'origin':1000000000,'scan_duration_seconds':1})['hypotheses'][0]['fits'])
