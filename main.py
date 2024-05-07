# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def solveQuadraticEquation(a, b, c):
    raiz1 = (-b + (b**2 - 4 * a * c)**(1/2)) / (2 * a)
    raiz2 = (-b - (b**2 - 4 * a * c)**(1/2)) / (2 * a)
    print(raiz1, raiz2)
    
solveQuadraticEquation(1, -3, 2)