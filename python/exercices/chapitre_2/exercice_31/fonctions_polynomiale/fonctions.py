def fonction1(a: int, b: int, c: int, d: int, x: int) -> int :
    """Calcule une fonction polynomiale f définie tel que f(x) = ax^3 + bx^2 + cx + d"""
    result = a*(x**3) + b*(x**2) + c*x + d
    return result

def fonction2(a: int, b: int, c: int, x: int) -> int :
    """Calcule une fonction polynomiale f définie tel que f(x) = ax^4 + bx^2 + c"""
    result = a*(x**4) + b*(x**2) + c
    return result
