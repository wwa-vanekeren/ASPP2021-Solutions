"""
A collection of simple math operations
"""


""" 
The length of docstring lines should be kept to 75 characters to facilitate reading the docstrings in text terminals.

"""



def simple_add(a,b):
    """
    The sum of two numbers, a and b.

    .. deprecated:: #oldversion 
                `object_old` will be removed in #newversion, it is replaced by
                `object_new` because reason of improvement.
                
    Parameters
    ----------
    a: int
        Variable
    b: int 
        Variable
    
    Returns
    ----------
    int
        Description of anonymous integer return value.
        
        Yields #only relevant in generators
    ------
    int
        Description of the anonymous integer return value.
    
    etc. 
    """
    return a+b

def simple_sub(a,b):
    """
    Definition for the difference between two numbers, a and b. 
                
    Parameters
    ----------
    a: int
        Variable
    b: int 
        Variable
    
    Returns
    ----------
    int
        Description of anonymous integer return value.
        
        Yields #only relevant in generators
    ------
    int
        Description of the anonymous integer return value.
    
    etc. 
    """
    return a-b

def simple_mult(a,b):
    """
    Definition for the multiplication of two numbers, a and b. 
                
    Parameters
    ----------
    a: int
        Variable
    b: int 
        Variable
    
    Returns
    ----------
    int
        Description of anonymous integer return value.
        
        Yields #only relevant in generators
    ------
    int
        Description of the anonymous integer return value.
    
    etc. 
    """
    return a*b

def simple_div(a,b):
    """
    Definition for the fraction of two numbers, a and b. 
                
    Parameters
    ----------
    a: int
        Variable
    b: int 
        Variable
    
    Returns
    ----------
    int
        Description of anonymous integer return value.
        
        Yields #only relevant in generators
    ------
    int
        Description of the anonymous integer return value.
    
    etc. 
    """
    return a/b

def poly_first(x, a0, a1):
    """
    First order polynomial.
    
    Parameters
    ----------
    x : int,float
        Variable in the polynomial.
        
    a0 : int, float
        Coefficient for the constant in the polynomial.
        
    a1 : int, float
        Coefficient for the first order variable in the polynonmial.
        
    Returns
    ----------
    int, float
        The first order polynomial evaluated at `x` with the given coefficients.
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    Second order polynomial.
    
    Parameters
    ----------
    x : int,float
        Variable in the polynomial.
        
    a0 : int, float
        Coefficient1 for the constant in the polynomial.
        
    a1 : int, float
        Coefficient2 for the second order variable in the polynonmial.
        
    a2: int, float
        Coefficient3 for the second order variable in the polynonmial.    
        
    Returns
    ----------
    int, float
        The second order polynomial in the form y = a0 + a1*x.
    """    
    
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
