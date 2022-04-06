# This is a sample Python script.
import sympy
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from sympy import Matrix, diag, symbols, init_printing, pprint, factor

init_printing()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def find_w():
    pprint(factor(C * ((diag(s, s, s, s) - A).inv() * B)))


s = symbols('s')
A = Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [2, -2, -5, -2], [-5, -1 / 5, 0, -3]])
B = Matrix([[0], [0], [-1], [1]])
C = Matrix([1, 1, 0, 0]).transpose()
find_w()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
