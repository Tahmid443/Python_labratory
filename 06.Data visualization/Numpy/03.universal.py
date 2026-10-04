import numpy as np

# numpy universal functions
np1 = np.array([0,1,2,3,4,5,6,7,8,9])
np2 = np.array([-3,-2,-1,0,1,2,3])
print(np1)

# square root of each element
print(np.sqrt(np1))

# absolute value
print(np.absolute(np2))

# exponentials
print(np.exp(np1))

# min/max
print(np.max(np1))
print(np.min(np1))

# sign positive or negative
print(np.sign(np2))

# trig sin cos log
print(np.log(np1))
print(np.sin(np1))



"""
================================================================================
        NUMPY UNIVERSAL FUNCTIONS (ufuncs) - COMPLETE LIST WITH DESCRIPTIONS
================================================================================
"""

import numpy as np

# ==============================================================================
# 1. MATH OPERATIONS (Binary ufuncs)
# ==============================================================================
np.add  # Element-wise addition (x1 + x2)
np.subtract  # Element-wise subtraction (x1 - x2)
np.multiply  # Element-wise multiplication (x1 * x2)
np.divide  # Element-wise true division (x1 / x2)
np.true_divide  # Same as divide (x1 / x2)
np.floor_divide  # Element-wise floor division (x1 // x2)
np.mod  # Element-wise modulus (x1 % x2)
np.remainder  # Same as mod (x1 % x2)
np.fmod  # C-style modulus (sign follows dividend)
np.power  # Element-wise exponentiation (x1 ** x2)
np.float_power  # Power with float precision (avoids overflow)
np.divmod  # Returns (quotient, remainder) pair
np.negative  # Element-wise negation (-x)
np.positive  # Element-wise positive (+x)
np.absolute  # Element-wise absolute value |x|
np.abs  # Alias of absolute
np.fabs  # Fast absolute value (always float)
np.rint  # Round to nearest integer
np.sign  # Sign of each element (-1, 0, or +1)
np.heaviside  # Heaviside step function
np.conjugate  # Complex conjugate
np.conj  # Alias of conjugate
np.angle  # Angle of complex number
np.gcd  # Greatest common divisor
np.lcm  # Least common multiple

# ==============================================================================
# 2. TRIGONOMETRIC FUNCTIONS
# ==============================================================================
np.sin  # Sine (element-wise)
np.cos  # Cosine (element-wise)
np.tan  # Tangent (element-wise)
np.arcsin  # Inverse sine
np.arccos  # Inverse cosine
np.arctan  # Inverse tangent
np.arctan2  # Inverse tangent of x1/x2 with correct quadrant
np.sinh  # Hyperbolic sine
np.cosh  # Hyperbolic cosine
np.tanh  # Hyperbolic tangent
np.arcsinh  # Inverse hyperbolic sine
np.arccosh  # Inverse hyperbolic cosine
np.arctanh  # Inverse hyperbolic tangent
np.deg2rad  # Convert degrees → radians
np.rad2deg  # Convert radians → degrees
np.degrees  # Alias of rad2deg
np.radians  # Alias of deg2rad

# ==============================================================================
# 3. EXPONENTIAL & LOGARITHMIC
# ==============================================================================
np.exp  # e^x
np.exp2  # 2^x
np.expm1  # e^x - 1 (accurate for small x)
np.log  # Natural logarithm
np.log2  # Base-2 logarithm
np.log10  # Base-10 logarithm
np.log1p  # log(1 + x) (accurate for small x)
np.logaddexp  # log(exp(x1) + exp(x2)) — numerically stable
np.logaddexp2  # log2(2^x1 + 2^x2)

# ==============================================================================
# 4. POWER & ROOT
# ==============================================================================
np.sqrt  # Square root
np.cbrt  # Cube root
np.square  # x²
np.reciprocal  # 1/x

# ==============================================================================
# 5. ROUNDING & TRUNCATION
# ==============================================================================
np.round  # Round to given decimals
np.around  # Alias of round
np.floor  # Largest integer ≤ x
np.ceil  # Smallest integer ≥ x
np.trunc  # Truncate toward zero
np.fix  # Round toward zero (returns float)

# ==============================================================================
# 6. COMPARISON FUNCTIONS (Return boolean arrays)
# ==============================================================================
np.greater  # x1 > x2
np.greater_equal  # x1 >= x2
np.less  # x1 < x2
np.less_equal  # x1 <= x2
np.equal  # x1 == x2
np.not_equal  # x1 != x2
np.logical_and  # Logical AND
np.logical_or  # Logical OR
np.logical_xor  # Logical XOR
np.logical_not  # Logical NOT
np.isnan  # True where NaN
np.isinf  # True where ±inf
np.isfinite  # True where finite (not NaN/inf)
np.isposinf  # True where +inf
np.isneginf  # True where -inf
np.signbit  # True where sign bit is set (negative)
np.copysign  # Magnitude of x1 with sign of x2

# ==============================================================================
# 7. MAXIMUM / MINIMUM
# ==============================================================================
np.maximum  # Element-wise maximum
np.minimum  # Element-wise minimum
np.fmax  # Element-wise max, ignoring NaN
np.fmin  # Element-wise min, ignoring NaN
np.clip  # Clip values to a range [min, max]

# ==============================================================================
# 8. BITWISE OPERATIONS (Integer types only)
# ==============================================================================
np.bitwise_and  # Bitwise AND (x1 & x2)
np.bitwise_or  # Bitwise OR (x1 | x2)
np.bitwise_xor  # Bitwise XOR (x1 ^ x2)
np.invert  # Bitwise NOT (~x)
np.left_shift  # Left shift (x1 << x2)
np.right_shift  # Right shift (x1 >> x2)

# ==============================================================================
# 9. FLOATING-POINT / SPECIAL MATH
# ==============================================================================
np.nextafter  # Next representable float after x1 toward x2
np.spacing  # Distance between x and next adjacent float
np.ldexp  # x1 * 2^x2 (inverse of frexp)
np.frexp  # Decompose x into mantissa and exponent
np.modf  # Split into fractional and integral parts
np.floor_divide  # Floor division
np.copysign  # Copy sign from x2 to x1

# ==============================================================================
# 10. SPECIAL FUNCTIONS (scipy.special also provides more)
# ==============================================================================
np.i0  # Modified Bessel function of order 0
np.sinc  # Normalized sinc function sin(πx)/(πx)

# ==============================================================================
# 11. DATETIME / TIMEDELTA UFUNCS
# ==============================================================================
np.isnat  # True where NaT (Not-a-Time)
np.datetime_data  # Get datetime unit and step

# ==============================================================================
# 12. FLOATING POINT PREDICATES
# ==============================================================================
np.isnan  # True where NaN
np.isinf  # True where infinity
np.isfinite  # True where finite
np.isposinf  # True where +inf
np.isneginf  # True where -inf
np.signbit  # True if sign bit set (negative)

# ==============================================================================
# 13. STRING UFUNCS (Also available in numpy.char module)
# ==============================================================================
# These operate on string/unicode arrays
np.char.add  # Element-wise string concatenation
np.char.multiply  # Repeat string element-wise
np.char.mod  # Element-wise string formatting
np.char.capitalize  # Capitalize first char
np.char.center  # Center string in field
np.char.decode  # Decode bytes to str
np.char.encode  # Encode str to bytes
np.char.expandtabs  # Expand tabs to spaces
np.char.join  # Join strings with separator
np.char.ljust  # Left-justify in field
np.char.lower  # Convert to lowercase
np.char.lstrip  # Strip chars from left
np.char.partition  # Partition around separator
np.char.replace  # Replace substring
np.char.rjust  # Right-justify in field
np.char.rpartition  # Partition from right
np.char.rsplit  # Split from right
np.char.rstrip  # Strip chars from right
np.char.split  # Split string
np.char.splitlines  # Split at line boundaries
np.char.strip  # Strip chars from both ends
np.char.swapcase  # Swap uppercase/lowercase
np.char.title  # Title-case
np.char.translate  # Translate characters
np.char.upper  # Convert to uppercase
np.char.zfill  # Zero-fill numeric strings

# ==============================================================================
# 14. SUMMARY — CATEGORY COUNT
# ==============================================================================
"""
Category                      | Count (approx.)
------------------------------|----------------
Math operations               | 25+
Trigonometric                 | 18+
Exponential / Logarithmic     | 9
Power & Root                  | 4
Rounding                      | 6
Comparison                    | 15+
Max / Min                     | 5
Bitwise                       | 6
Floating-point special        | 6
Special math functions        | 2
Datetime                      | 2
String (numpy.char)           | 30+

Total ~ 130+ ufuncs across all categories.
"""
