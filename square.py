def area(a: float) -> float:
    '''
    Return area of square.

    Pararmeters:
    ------------
        a (float): first number.

    Return:
    -------
        area (float): area of a square with side `a`.

    Eximples:
    ---------
        >>> area(2)
        4
    '''
    if a < 0:
        raise ValueError("Negative number")
    return a * a

def perimeter(a: float) -> float:
    '''
    Return perimeter of square.

    Pararmeters:
    ------------
        a (float): first number.

    Return:
    -------
        perimeter (float): perimeter of a square with side `a`.

    Eximples:
    ---------
        >>> perimeter(2)
        8
    '''
    if a < 0:
        raise ValueError("Negative number")
    return 4 * a
