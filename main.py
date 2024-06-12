from typing import List, Union

def solve_single_quadratic(a: float, b: float, c: float) -> List[Union[float, str]]:
    """
    Calculates the root of a single quadratic equation of the form a*x^2 + b*x + c = 0
    :param a: coefficient of x^2
    :type a: float
    :param b: coefficient of x
    :type b: float
    :param c: constant
    :type c: float
    :return: A list (in increasing order) of the roots of the equation. If there's no root, the function returns 'NA'
    :rtype: List[Union[float, str]]
    """
    try:
        # Calculate the discriminant
        discriminant = b**2 - 4 * a * c
        if discriminant > 0:
            # For the case of two distinct real roots
            raiz1 = (-b - (discriminant)**(1/2)) / (2 * a)
            raiz2 = (-b + (discriminant)**(1/2)) / (2 * a)
        elif discriminant == 0:
            # One real root
            raiz1 = (-b + (discriminant) ** (1 / 2)) / (2 * a)
            raiz2 = "NA"
        else:
            # No real roots
            raiz1 = "NA"
            raiz2 = "NA"
        return [raiz1, raiz2]
    except Exception as e:
        # In case of error, return an error message
        return [f"Error: {e}"]


def solve_quadratics(a: List[float], b: List[float], c: List[float]) -> List[List[Union[float , str ]]]:
    """
    Calculates the root of multiples quadratics equations of the form a*x^2 + b*x + c = 0
    :param a: List of coefficient for x^2
    :type a: List[float]
    :param b: List of coefficient for x
    :type b: List[float]
    :param c: List of constant terms
    :type c: List[float]
    :return: A list of lists containing the roots (in increasing order) of each quadratic equation. If there's no root, the function returns 'NA'
    :rtype: List[List[Union[float, str]]]
    """
    # Check if all lists have the same length
    if len(a) != len(b) or len(a) != len(c) or len(b) != len(c):
        return [["Error: All input lists must have the same length"]]

    raizes = []
    # Use a loop in order iterate over each set of coefficients
    for i in range(len(a)):
        try:
            # Solve the equation for the current coefficients and append to the raizes list
            raizes.append(solve_single_quadratic(a[i], b[i], c[i]))
        except Exception as e:
            # Append an error message in case of error
            raizes.append([f"Error: {e}"])
    return raizes

