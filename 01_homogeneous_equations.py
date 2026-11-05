import sympy as sp

x = sp.symbols('x')
y = sp.Function('y')

# Define the differential equation
ode = sp.Eq(
    sp.diff(y(x), x, 2)
    - 3*sp.diff(y(x), x)
    + 2*y(x), 0
)

# Solve the equation
solution = sp.dsolve(ode)

print("Differential equation:")
sp.pprint(ode)

print("\nGeneral solution:")
sp.pprint(solution)
