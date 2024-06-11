from typing import List, Union

def solve_single_quadratic(a: float, b: float, c: float) -> List[Union[float, str]]:
    """
    Calculates the root of a single quadratic equation of the form a*x^2 + b*x + c = 0
    :parameter a: coefficient of x^2
    :parameter b: coefficient of x
    :parameter c: constant
    :return: A list (in increasing order) of the roots of the equation. If there's no root, the function returns 'NA'
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
    :parameter a: List of coefficient for x^2
    :parameter b: List of coefficient for x
    :parameter c: List of constant terms
    :return: A list of lists containing the roots (in increasing order) of each quadratic equation. If there's no root, the function returns 'NA'
    """
    # Check if all lists have the same length
    if len(a) != len(b) or len(a) != len(c) or len(b) != len(c):
        return [["Error: All input lists must have the same length"]]

    raizes = []
    # Use a loop in order to solve for each quadratic equation
    for i in range(len(a)):
        try:
            raizes.append(solve_single_quadratic(a[i], b[i], c[i]))
        except Exception as e:
            # Append an error message in case of error
            raizes.append([f"Error: {e}"])
    return raizes

a = [2, 1, 3]
b = [-3, -6, -2]
c = [-2, 9, 1]

print(solve_quadratics(a, b, c))
