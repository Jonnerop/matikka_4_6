import numpy as np
from sympy import symbols, diff


#tehtävä 1.


x = symbols('x')
derivative = diff(2*x**2-3, x)

#tehtävä 2.


def f(x):
    return np.sin(x)


dx = 0.001
x = 2
two_point_derivative = (f(x + dx) - f(x)) / dx
three_point_derivative = (f(x + dx) - f(x - dx)) / (2*dx)

#tehtävä 3.


def f(x1):
    return np.exp(-x1**2)


x1 = 1.5
dx1 = 0.001
three_point_derivative_two = (f(x1 + dx1) - f(x1 - dx1)) / (2*dx1)


#tehtävä 4.


def calculate_derivative(delta_x, f_x, f_x_plus_delta_x):
    derivative_approx = (f_x_plus_delta_x - f_x) / delta_x
    return derivative_approx


x1 = -4
delta_x1 = 0.5
f_x1 = -6
f_x_plus_delta_x1 = -7
derivative1 = calculate_derivative(delta_x1, f_x1, f_x_plus_delta_x1)

x2 = -0.5
delta_x2 = 0.5
f_x2 = 2.5
f_x_plus_delta_x2 = 3
derivative2 = calculate_derivative(delta_x2, f_x2, f_x_plus_delta_x2)

x3 = 3
delta_x3 = 0.5
f_x3 = 10
f_x_plus_delta_x3 = 18
derivative3 = calculate_derivative(delta_x3, f_x3, f_x_plus_delta_x3)

print('Funktion f(x)=2x^2-3 derivaatta on', derivative)
print('Funktion f(x)=sinx derivaatta kaksipistekaavalla on', two_point_derivative)
print('Funktion f(x)=sinx derivaatta kolmepistekaavalla on', three_point_derivative)
print('Funktion f(x)=e^(-x^2) derivaatta kolmepistekaavalla on', three_point_derivative_two)
print('Aproksimoitu derivaatta kohdassa x =', x1, 'is', derivative1)
print('Aproksimoitu derivaatta kohdassa x =', x2, 'is', derivative2)
print('Aproksimoitu derivaatta kohdassa x =', x3, 'is', derivative3)

