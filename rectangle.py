def area(a: float, b: float) -> float:
    '''
    Return area of rectangle.

    Pararmeters:
    ------------
        a (float): first number.
        b (float): second number.

    Return:
    -------
        area (float): area of a rectangle with sides `a` and `b`.

    Eximples:
    ---------
        >>> area(1, 2)
        2
    '''
    if a < 0 or b < 0:
        raise ValueError("Negative numbers")
    return a * b

def perimeter(a: float, b: float) -> float:
    '''
    Return perimeter of rectangle.

    Pararmeters:
    ------------
        a (float): first number.
        b (float): second number.

    Return:
    -------
        perimeter (float): perimeter of a rectangle with sides `a` and `b`.

    Eximples:
    ---------
        >>> perimeter(1, 2)
        6
    '''
    if a < 0 or b < 0:
        raise ValueError("Negative numbers")
    return (a + b) * 2
