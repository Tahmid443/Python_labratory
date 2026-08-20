"""
================================================================================
MATH MODULE - COMPLETE METHOD REFERENCE (A TO Z)
================================================================================

All methods from Python's built-in math module, sorted alphabetically.

================================================================================
COMPLETE METHOD LIST WITH DESCRIPTIONS
================================================================================

math.acos()         Returns the arc cosine of a number
math.acosh()        Returns the inverse hyperbolic cosine of a number
math.asin()         Returns the arc sine of a number
math.asinh()        Returns the inverse hyperbolic sine of a number
math.atan()         Returns the arc tangent of a number in radians
math.atan2()        Returns the arc tangent of y/x in radians
math.atanh()        Returns the inverse hyperbolic tangent of a number
math.ceil()         Rounds a number up to the nearest integer
math.comb()         Returns the number of ways to choose k items from n items without repetition and order
math.copysign()     Returns a float consisting of the value of the first parameter and the sign of the second parameter
math.cos()          Returns the cosine of a number
math.cosh()         Returns the hyperbolic cosine of a number
math.degrees()      Converts an angle from radians to degrees
math.dist()         Returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point
math.erf()          Returns the error function of a number
math.erfc()         Returns the complementary error function of a number
math.exp()          Returns E raised to the power of x
math.expm1()        Returns Ex - 1
math.fabs()         Returns the absolute value of a number
math.factorial()    Returns the factorial of a number
math.floor()        Rounds a number down to the nearest integer
math.fmod()         Returns the remainder of x/y
math.frexp()        Returns the mantissa and the exponent, of a specified number
math.fsum()         Returns the sum of all items in any iterable (tuples, arrays, lists, etc.)
math.gamma()        Returns the gamma function at x
math.gcd()          Returns the greatest common divisor of two integers
math.hypot()        Returns the Euclidean norm
math.isclose()      Checks whether two values are close to each other, or not
math.isfinite()     Checks whether a number is finite or not
math.isinf()        Checks whether a number is infinite or not
math.isnan()        Checks whether a value is NaN (not a number) or not
math.isqrt()        Rounds a square root number downwards to the nearest integer
math.ldexp()        Returns the inverse of math.frexp() which is x * (2**i) of the given numbers x and i
math.lgamma()       Returns the log gamma value of x
math.log()          Returns the natural logarithm of a number, or the logarithm of number to base
math.log10()        Returns the base-10 logarithm of x
math.log1p()        Returns the natural logarithm of 1+x
math.log2()         Returns the base-2 logarithm of x
math.perm()         Returns the number of ways to choose k items from n items with order and without repetition
math.pow()          Returns the value of x to the power of y
math.prod()         Returns the product of all the elements in an iterable
math.radians()      Converts a degree value into radians
math.remainder()    Returns the closest value that can make numerator completely divisible by the denominator
math.sin()          Returns the sine of a number
math.sinh()         Returns the hyperbolic sine of a number
math.sqrt()         Returns the square root of a number
math.tan()          Returns the tangent of a number
math.tanh()         Returns the hyperbolic tangent of a number
math.trunc()        Returns the truncated integer parts of a number

================================================================================
CATEGORY-WISE ORGANIZATION
================================================================================

1. TRIGONOMETRIC FUNCTIONS
   math.acos()      math.acosh()     math.asin()      math.asinh()
   math.atan()      math.atan2()     math.atanh()     math.cos()
   math.cosh()      math.sin()       math.sinh()      math.tan()
   math.tanh()

2. ANGLE CONVERSION
   math.degrees()   math.radians()

3. LOGARITHMIC & EXPONENTIAL FUNCTIONS
   math.exp()       math.expm1()     math.log()       math.log10()
   math.log1p()     math.log2()

4. POWER & ROOT FUNCTIONS
   math.pow()       math.sqrt()      math.isqrt()     math.hypot()

5. ROUNDING FUNCTIONS
   math.ceil()      math.floor()     math.trunc()     math.fmod()
   math.remainder()

6. COMBINATORICS
   math.comb()      math.perm()      math.factorial()

7. NUMERIC UTILITIES
   math.fabs()      math.copysign()  math.frexp()     math.ldexp()
   math.gcd()       math.fsum()      math.prod()      math.dist()

8. ERROR & GAMMA FUNCTIONS
   math.erf()       math.erfc()      math.gamma()     math.lgamma()

9. CHECKING FUNCTIONS
   math.isclose()   math.isfinite()  math.isinf()     math.isnan()

================================================================================
FULL CODE REFERENCE WITH PARAMETERS AND DESCRIPTIONS
================================================================================
"""

import math

# ==============================================================================
# 1. TRIGONOMETRIC FUNCTIONS
# ==============================================================================

# math.acos(x) - Arc cosine in radians (x in [-1, 1])
math.acos(0.5)  # 1.0471975511965979

# math.acosh(x) - Inverse hyperbolic cosine (x >= 1)
math.acosh(2)  # 1.3169578969248166

# math.asin(x) - Arc sine in radians (x in [-1, 1])
math.asin(0.5)  # 0.5235987755982989

# math.asinh(x) - Inverse hyperbolic sine
math.asinh(2)  # 1.4436354751788103

# math.atan(x) - Arc tangent in radians
math.atan(1)  # 0.7853981633974483

# math.atan2(y, x) - Arc tangent of y/x in radians (handles quadrant)
math.atan2(1, 1)  # 0.7853981633974483

# math.atanh(x) - Inverse hyperbolic tangent (x in [-1, 1])
math.atanh(0.5)  # 0.5493061443340549

# math.cos(x) - Cosine of x (x in radians)
math.cos(math.pi)  # -1.0

# math.cosh(x) - Hyperbolic cosine
math.cosh(0)  # 1.0

# math.sin(x) - Sine of x (x in radians)
math.sin(math.pi / 2)  # 1.0

# math.sinh(x) - Hyperbolic sine
math.sinh(0)  # 0.0

# math.tan(x) - Tangent of x (x in radians)
math.tan(math.pi / 4)  # 0.9999999999999999

# math.tanh(x) - Hyperbolic tangent
math.tanh(0)  # 0.0

# ==============================================================================
# 2. ANGLE CONVERSION
# ==============================================================================

# math.degrees(x) - Convert radians to degrees
math.degrees(math.pi)  # 180.0
math.degrees(math.pi / 2)  # 90.0

# math.radians(x) - Convert degrees to radians
math.radians(180)  # 3.141592653589793
math.radians(90)  # 1.5707963267948966

# ==============================================================================
# 3. LOGARITHMIC & EXPONENTIAL FUNCTIONS
# ==============================================================================

# math.exp(x) - e raised to power x
math.exp(1)  # 2.718281828459045
math.exp(0)  # 1.0

# math.expm1(x) - e^x - 1 (accurate for small x)
math.expm1(1)  # 1.718281828459045
math.expm1(0.001)  # 0.0010005001667083846

# math.log(x[, base]) - Natural logarithm (or log to specified base)
math.log(math.e)  # 1.0
math.log(100, 10)  # 2.0

# math.log10(x) - Base-10 logarithm
math.log10(100)  # 2.0
math.log10(1000)  # 3.0

# math.log1p(x) - Natural logarithm of (1+x) (accurate for small x)
math.log1p(1)  # 0.6931471805599453
math.log1p(0.001)  # 0.0009995003330835331

# math.log2(x) - Base-2 logarithm
math.log2(8)  # 3.0
math.log2(16)  # 4.0

# ==============================================================================
# 4. POWER & ROOT FUNCTIONS
# ==============================================================================

# math.pow(x, y) - x raised to power y
math.pow(2, 3)  # 8.0
math.pow(10, -2)  # 0.01

# math.sqrt(x) - Square root of x
math.sqrt(16)  # 4.0
math.sqrt(2)  # 1.4142135623730951

# math.isqrt(x) - Integer square root (rounded down)
math.isqrt(16)  # 4
math.isqrt(17)  # 4 (floor of sqrt)

# math.hypot(*coordinates) - Euclidean norm (distance from origin)
math.hypot(3, 4)  # 5.0
math.hypot(1, 2, 3)  # 3.7416573867739413

# ==============================================================================
# 5. ROUNDING FUNCTIONS
# ==============================================================================

# math.ceil(x) - Round up to nearest integer
math.ceil(4.2)  # 5
math.ceil(-4.2)  # -4

# math.floor(x) - Round down to nearest integer
math.floor(4.8)  # 4
math.floor(-4.8)  # -5

# math.trunc(x) - Truncate to integer (towards zero)
math.trunc(4.8)  # 4
math.trunc(-4.8)  # -4

# math.fmod(x, y) - Remainder of x/y (float, sign of x)
math.fmod(10, 3)  # 1.0
math.fmod(-10, 3)  # -1.0

# math.remainder(x, y) - Closest value making x divisible by y
math.remainder(10, 3)  # 1.0
math.remainder(10, 4)  # 2.0

# ==============================================================================
# 6. COMBINATORICS
# ==============================================================================

# math.comb(n, k) - Number of combinations (n choose k) without repetition
math.comb(5, 2)  # 10
math.comb(10, 3)  # 120

# math.perm(n, k) - Number of permutations (n pick k) with order
math.perm(5, 2)  # 20
math.perm(10, 3)  # 720

# math.factorial(x) - Factorial of x (x >= 0, integer)
math.factorial(5)  # 120
math.factorial(0)  # 1

# ==============================================================================
# 7. NUMERIC UTILITIES
# ==============================================================================

# math.fabs(x) - Absolute value (returns float)
math.fabs(-5)  # 5.0
math.fabs(3.14)  # 3.14

# math.copysign(x, y) - Return x with sign of y
math.copysign(5, -1)  # -5.0
math.copysign(-5, 1)  # 5.0

# math.frexp(x) - Returns (mantissa, exponent) of x
math.frexp(10)  # (0.625, 4) meaning 10 = 0.625 * 2^4
math.frexp(0.5)  # (0.5, 0)

# math.ldexp(x, i) - Returns x * (2**i) (inverse of frexp)
math.ldexp(0.625, 4)  # 10.0
math.ldexp(0.5, 0)  # 0.5

# math.gcd(a, b) - Greatest common divisor
math.gcd(12, 18)  # 6
math.gcd(100, 35)  # 5

# math.fsum(iterable) - Accurate sum of floating point numbers
math.fsum([0.1, 0.2, 0.3])  # 0.6
math.fsum([1, 2, 3, 4, 5])  # 15.0

# math.prod(iterable) - Product of all elements in iterable
math.prod([1, 2, 3, 4])  # 24
math.prod([2, 3, 5])  # 30

# math.dist(p, q) - Euclidean distance between two points
math.dist([0, 0], [3, 4])  # 5.0
math.dist([1, 1], [4, 5])  # 5.0

# ==============================================================================
# 8. ERROR & GAMMA FUNCTIONS
# ==============================================================================

# math.erf(x) - Error function (probability)
math.erf(0)  # 0.0
math.erf(1)  # 0.8427007929497149

# math.erfc(x) - Complementary error function (1 - erf(x))
math.erfc(0)  # 1.0
math.erfc(1)  # 0.1572992070502851

# math.gamma(x) - Gamma function
math.gamma(5)  # 24.0 (same as 4!)
math.gamma(0.5)  # 1.772453850905516 (sqrt(pi))

# math.lgamma(x) - Natural log of absolute value of gamma(x)
math.lgamma(5)  # 3.1780538303479458
math.lgamma(0.5)  # 0.5723649429247001

# ==============================================================================
# 9. CHECKING FUNCTIONS
# ==============================================================================

# math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0) - Check if values are close
math.isclose(0.1 + 0.2, 0.3)  # True
math.isclose(1.0, 1.0000001)  # True
math.isclose(1.0, 1.1, rel_tol=0.05)  # True

# math.isfinite(x) - Check if x is finite (not inf or NaN)
math.isfinite(5)  # True
math.isfinite(float("inf"))  # False
math.isfinite(float("nan"))  # False

# math.isinf(x) - Check if x is infinite
math.isinf(float("inf"))  # True
math.isinf(float("-inf"))  # True
math.isinf(5)  # False

# math.isnan(x) - Check if x is NaN (Not a Number)
math.isnan(float("nan"))  # True
math.isnan(5)  # False

# ==============================================================================
# COMPLETE REFERENCE SUMMARY TABLE
# ==============================================================================

"""
FUNCTION                PARAMETERS           RETURNS           DESCRIPTION
----------------------  -------------------  ----------------  -------------------------
acos(x)                 x in [-1,1]          float             Arc cosine
acosh(x)                x >= 1               float             Inverse hyperbolic cosine
asin(x)                 x in [-1,1]          float             Arc sine
asinh(x)                any float            float             Inverse hyperbolic sine
atan(x)                 any float            float             Arc tangent
atan2(y, x)             any float, any float float             Arc tangent of y/x
atanh(x)                x in [-1,1]          float             Inverse hyperbolic tangent
ceil(x)                 any float            int               Round up
comb(n, k)              n >= k >= 0          int               Combinations
copysign(x, y)          any float, any float float             Copy sign
cos(x)                  any float            float             Cosine
cosh(x)                 any float            float             Hyperbolic cosine
degrees(x)              any float            float             Radians to degrees
dist(p, q)              iterables            float             Euclidean distance
erf(x)                  any float            float             Error function
erfc(x)                 any float            float             Complementary error
exp(x)                  any float            float             e to power x
expm1(x)                any float            float             e^x - 1
fabs(x)                 any float            float             Absolute value
factorial(x)            x >= 0 integer       int               Factorial
floor(x)                any float            int               Round down
fmod(x, y)              any float, any float float             Remainder of x/y
frexp(x)                any float            tuple             Mantissa and exponent
fsum(iterable)          iterable             float             Sum (accurate)
gamma(x)                x != negative int    float             Gamma function
gcd(a, b)               integers             int               Greatest common divisor
hypot(*coords)          coordinates          float             Euclidean norm
isclose(a, b)           any float, any float bool              Check closeness
isfinite(x)             any float            bool              Check if finite
isinf(x)                any float            bool              Check if infinite
isnan(x)                any float            bool              Check if NaN
isqrt(x)                x >= 0 integer       int               Integer square root
ldexp(x, i)             any float, int       float             x * (2**i)
lgamma(x)               any float            float             Log gamma
log(x, base)            x > 0, base > 0      float             Logarithm
log10(x)                x > 0                float             Base-10 log
log1p(x)                x > -1               float             Log of (1+x)
log2(x)                 x > 0                float             Base-2 log
perm(n, k)              n >= k >= 0          int               Permutations
pow(x, y)               any float, any float float             x to power y
prod(iterable)          iterable             float             Product of elements
radians(x)              any float            float             Degrees to radians
remainder(x, y)         any float, any float float             Closest divisible value
sin(x)                  any float            float             Sine
sinh(x)                 any float            float             Hyperbolic sine
sqrt(x)                 x >= 0               float             Square root
tan(x)                  any float            float             Tangent
tanh(x)                 any float            float             Hyperbolic tangent
trunc(x)                any float            int               Truncate to integer

================================================================================
CONSTANTS AVAILABLE IN MATH MODULE
================================================================================

math.pi          # 3.141592653589793
math.e           # 2.718281828459045
math.tau         # 6.283185307179586 (2*pi)
math.inf         # float('inf')
math.nan         # float('nan')
math.sqrt(2)     # 1.4142135623730951 (sqrt2 constant)

================================================================================
"""
