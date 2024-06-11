from typing import List, Union

def solve_single_quadratic(a: float, b: float, c: float) -> List[Union[float, str]]:
    try:
        discriminant = b**2 - 4 * a * c
        if discriminant > 0:
            raiz1 = (-b - (b ** 2 - 4 * a * c)**(1/2)) / (2 * a)
            raiz2 = (-b + (b ** 2 - 4 * a * c)**(1/2)) / (2 * a)
        elif discriminant == 0:
            raiz1 = (-b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
            raiz2 = "NA"
        else:
            raiz1 = "NA"
            raiz2 = "NA"
        return raiz1, raiz2
    except Exception as e:
        return [f"Error: {e}"]


def solve_quadratics(a: List[float], b: List[float], c: List[float]) -> List[List[Union[float , str ]]]:
    if len(a) != len(b) or len(a) != len(c) or len(b) != len(c):
        return [["Error: All input lists must have the same length"]]

    raizes = []
    for i in range(len(a)):
        try:
            raizes.append(solve_single_quadratic(a[i], b[i], c[i]))
        except Exception as e:
            raizes.append([f"Error: {e}"])
    return raizes

a = [2, 1, 3]
b = [-3, -6, -2]
c = [-2, 9, 1]

print(solve_quadratics(a, b, c))
