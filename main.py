# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def solveQuadraticEquation(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        raiz1 = (-b + (b ** 2 - 4 * a * c)**(1/2)) / (2 * a)
        raiz2 = (-b - (b ** 2 - 4 * a * c)**(1/2)) / (2 * a)
    elif discriminant == 0:
        raiz1 = (-b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
        raiz2 = "NA"
    else:
        raiz1 = "NA"
        raiz2 = "NA"
    return raiz1, raiz2

def solve_quadratics(a, b, c):
    raizes = []
    for i in range(len(a)):
        raizes.append(solveQuadraticEquation(a[i], b[i], c[i]))
    return raizes

a = [2, 1, 3]
b = [-3, -6, -2]
c = [-2, 9, 1]

print(solve_quadratics(a, b, c))