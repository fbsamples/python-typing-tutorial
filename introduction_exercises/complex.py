# Purpose: Get familiar with more datatypes: float and complex,
# as well as practice with optional

def to_complex(a_component b_component):
    """ Construct a complex number (a_component + (i * b_component)),
    where a_component and b_component default to 0 if passed in as None.
    """
    a = 0.0
    if isinstance(a_component, float):
        a = a_component
    b = 0.0
    if isinstance(b_component, float):
        b = b_component
    return complex(a, b)
