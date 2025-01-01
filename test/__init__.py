import sys
import pytest

sys.path.append('.')
import pnf

print(pnf.__version__)

def test_separation_distance():
  arg                       = 10E9
  result                    = pnf.separation_distance(arg)
  expected                  = 0.150
  assert(round(result, 3)) == expected
    
assert round(pnf.sampling_spacing(3E9), 3)     == 0.050