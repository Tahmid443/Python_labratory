"""
Python has a built-in module that you can use for mathematical tasks for complex numbers.

The methods in this module accepts int, float, and complex numbers. It even accepts Python objects that has a __complex__() or __float__() method.

The methods in this module almost always return a complex number. If the return value can be expressed as a real number, the return value has an imaginary part of 0.

The cmath module has a set of methods and constants.
"""
"""
================================================================================
CMATH MODULE - COMPLETE METHOD REFERENCE (COMPLEX NUMBERS)
================================================================================

All methods from Python's built-in cmath module for complex number operations.

================================================================================
COMPLETE METHOD LIST WITH DESCRIPTIONS
================================================================================

cmath.acos(x)           Returns the arc cosine value of x
cmath.acosh(x)          Returns the hyperbolic arc cosine of x
cmath.asin(x)           Returns the arc sine of x
cmath.asinh(x)          Returns the hyperbolic arc sine of x
cmath.atan(x)           Returns the arc tangent value of x
cmath.atanh(x)          Returns the hyperbolic arctangent value of x
cmath.cos(x)            Returns the cosine of x
cmath.cosh(x)           Returns the hyperbolic cosine of x
cmath.exp(x)            Returns the value of Ex, where E is Euler's number (approximately 2.718281...), and x is the number passed to it
cmath.isclose()         Checks whether two values are close, or not
cmath.isfinite(x)       Checks whether x is a finite number
cmath.isinf(x)          Check whether x is a positive or negative infinty
cmath.isnan(x)          Checks whether x is NaN (not a number)
cmath.log(x[, base])    Returns the logarithm of x to the base
cmath.log10(x)          Returns the base-10 logarithm of x
cmath.phase()           Return the phase of a complex number
cmath.polar()           Convert a complex number to polar coordinates
cmath.rect()            Convert polar coordinates to rectangular form
cmath.sin(x)            Returns the sine of x
cmath.sinh(x)           Returns the hyperbolic sine of x
cmath.sqrt(x)           Returns the square root of x
cmath.tan(x)            Returns the tangent of x
cmath.tanh(x)           Returns the hyperbolic tangent of x

================================================================================
IMPORT STATEMENT
================================================================================
"""
# ============================================================
# 1. IMPORTS
# ============================================================

# Option 1: use the module namespace
# cmath.sqrt(1 + 1j)

# Option 2: import individual functions
from cmath import (
    acos,
    acosh,
    asin,
    asinh,
    atan,
    atanh,
    cos,
    cosh,
    exp,
    isclose,
    isfinite,
    isinf,
    isnan,
    log,
    log10,
    phase,
    polar,
    rect,
    sin,
    sinh,
    sqrt,
    tan,
    tanh,
)

# ============================================================
# 2. TRIGONOMETRIC FUNCTIONS
# ============================================================

z = 1 + 2j

print("acos :", cmath.acos(z))
print("acosh:", cmath.acosh(z))
print("asin :", cmath.asin(z))
print("asinh:", cmath.asinh(z))
print("atan :", cmath.atan(z))
print("atanh:", cmath.atanh(z))

print("cos  :", cmath.cos(z))
print("cosh :", cmath.cosh(z))
print("sin  :", cmath.sin(z))
print("sinh :", cmath.sinh(z))
print("tan  :", cmath.tan(z))
print("tanh :", cmath.tanh(z))


# ============================================================
# 3. EXPONENTIAL & LOGARITHMIC FUNCTIONS
# ============================================================

print("exp  :", cmath.exp(z))
print("log  :", cmath.log(z))
print("log2 :", cmath.log(z, 2))
print("log10:", cmath.log10(z))


# ============================================================
# 4. CHECKING FUNCTIONS
# ============================================================

a = 1 + 1j
b = 1.00000001 + 1.00000001j

print("isclose  :", cmath.isclose(a, b))
print("isfinite :", cmath.isfinite(z))
print("isinf    :", cmath.isinf(z))
print("isnan    :", cmath.isnan(z))


# ============================================================
# 5. PHASE & POLAR COORDINATES
# ============================================================

z = 1 + 1j

angle = cmath.phase(z)
print("phase (radians):", angle)
print("phase (degrees):", math.degrees(angle))

r, theta = cmath.polar(z)
print("polar radius   :", r)
print("polar angle    :", theta)

z_rect = cmath.rect(r, theta)
print("rectangular    :", z_rect)


# ============================================================
# 6. COMPLEX SQUARE ROOT
# ============================================================

print("sqrt(1 + 0j):", cmath.sqrt(1 + 0j))
print("sqrt(-1 + 0j):", cmath.sqrt(-1 + 0j))
print("sqrt(1 + 1j):", cmath.sqrt(1 + 1j))


# ============================================================
# 7. CREATING COMPLEX NUMBERS
# ============================================================

z1 = 3 + 4j
z2 = complex(3, 4)
z3 = 1.5 - 2.5j
z4 = 0 + 0j

print("z1:", z1)
print("z2:", z2)
print("z3:", z3)
print("z4:", z4)


# ============================================================
# 8. ACCESSING COMPLEX-NUMBER COMPONENTS
# ============================================================

z = 3 + 4j

print("real     :", z.real)
print("imaginary:", z.imag)
print("conjugate:", z.conjugate())


# ============================================================
# 9. BASIC COMPLEX-NUMBER OPERATIONS
# ============================================================

a = 1 + 2j
b = 3 + 4j

print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division        :", a / b)
print("Power          :", a**2)


# ============================================================
# 10. PRACTICAL EXAMPLE: POLAR <-> RECTANGULAR
# ============================================================

z = 3 + 4j

r, theta = cmath.polar(z)
print("Polar form:", r, theta)

z_from_polar = cmath.rect(r, theta)
print("Back to rectangular:", z_from_polar)


# ============================================================
# 11. COMPLEX LOGARITHM
# ============================================================

z = -1 + 0j

print("log(-1):", cmath.log(z))
print("Expected form: pi*j")


# ============================================================
# 12. COMPLEX TRIGONOMETRIC IDENTITY
# ============================================================

z = 1 + 2j

result = cmath.cos(z) ** 2 + cmath.sin(z) ** 2
print("cos²(z) + sin²(z):", result)


# ============================================================
# 13. COMMON ERRORS / EXCEPTIONS
# ============================================================

# log(0) raises ValueError.
try:
    print(cmath.log(0 + 0j))
except ValueError as e:
    print("ValueError:", e)

# Very large exponential values can raise OverflowError.
try:
    print(cmath.exp(1000 + 1000j))
except OverflowError as e:
    print("OverflowError:", e)

# Division by zero raises ZeroDivisionError.
try:
    print((1 + 2j) / (0 + 0j))
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)


# ============================================================
# 14. MATH VS CMATH
# ============================================================

"""
math:
    - Primarily works with real numbers.
    - sqrt(-1) raises ValueError.

cmath:
    - Works with complex numbers.
    - sqrt(-1 + 0j) returns 1j.
    - Provides phase(), polar(), and rect().
"""

print("math.sqrt(4):", math.sqrt(4))
print("cmath.sqrt(-1 + 0j):", cmath.sqrt(-1 + 0j))


# ============================================================
# 15. QUICK REFERENCE
# ============================================================

"""
Function       Purpose
------------------------------------------------
acos(x)        Arc cosine
acosh(x)       Inverse hyperbolic cosine
asin(x)        Arc sine
asinh(x)       Inverse hyperbolic sine
atan(x)        Arc tangent
atanh(x)       Inverse hyperbolic tangent
cos(x)         Cosine
cosh(x)        Hyperbolic cosine
exp(x)         e raised to x
isclose(a,b)   Check whether values are close
isfinite(x)    Check whether x is finite
isinf(x)       Check whether x is infinite
isnan(x)       Check whether x is NaN
log(x[, base]) Logarithm
log10(x)       Base-10 logarithm
phase(x)       Phase/argument in radians
polar(x)       Convert to (r, theta)
rect(r, theta) Convert polar to rectangular
sin(x)         Sine
sinh(x)        Hyperbolic sine
sqrt(x)        Square root
tan(x)         Tangent
tanh(x)        Hyperbolic tangent
"""


# ============================================================
# END OF CMATH REFERENCE
# ============================================================
