"""
A collection of simple math operations
"""
#   the name of the test file should start with test_
#	the	name	of	the	testing	function	should		
#	also	start	with	test_	
import simple_math as sm
import numpy as np

def test_simple_add():
    assert sm.simple_add(1, 2) == 3

def test_simple_sub():
    assert sm.simple_sub(1, 2) == -1

def test_simple_mult():
    assert sm.simple_mult(3, 3) == 9

def test_simple_div():
    assert sm.simple_div(3, 3) == 1

def test_poly_first():
    assert sm.poly_first(1, -1, 1) == 0

# define variables for second poly test
a0 = np.random.rand(5)
a1 = np.random.rand(5)
a2 = np.random.rand(5)
a3 = np.random.rand(5)
solution = a0 + a1 * a3 + a2*a3

def test_poly_second(a3, a0, a1, a2):
    assert sm.poly_second(a3, a0, a1, a2) == solution

# Feel free to expand this list with more interesting mathematical operations...
# .....

