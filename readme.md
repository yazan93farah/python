# Summary Python 


 ## Python Operators – Priority and Associativity

| Priority (high → low) | Operator(s) | Description | Associativity |
|----------------------|-------------|-------------|---------------|
| 1 | `()` | Parentheses / grouping | left |
| 2 | `x[index]`, `x(args)`, `x.attr` | Indexing, function calls, attribute access | left |
| 3 | `**` | Exponentiation | **right** |
| 4 | `+x`, `-x`, `~x` | Unary plus, unary minus, bitwise NOT | right |
| 5 | `*`, `/`, `//`, `%` | Multiplication, division, floor division, modulo | left |
| 6 | `+`, `-` | Addition, subtraction | left |
| 7 | `<<`, `>>` | Bitwise shifts | left |
| 8 | `&` | Bitwise AND | left |
| 9 | `^` | Bitwise XOR | left |
| 10 | `\|` | Bitwise OR | left |
| 11 | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in` | Comparisons | left |
| 12 | `not` | Logical NOT | right |
| 13 | `and` | Logical AND | left |
| 14 | `or` | Logical OR | left |
| 15 | `if ... else` | Ternary conditional expression | right |
| 16 | `lambda` | Lambda expression | right |

> Higher priority = evaluated first.


## Common Python String Methods & Slicing

| Method / Syntax | Description |
|----------------|-------------|
| `splitlines()` | Splits the string at line breaks and returns a list of lines. |
| `strip()` | Removes leading and trailing whitespace (or specified characters). |
| `replace(old, new)` | Returns a new string with all occurrences of `old` replaced by `new`. |
| `count(sub)` | Returns the number of occurrences of substring `sub`. |
| `index(sub)` | Returns the first index of substring `sub`, raises an error if not found. |
| `find(sub)` | Returns the first index of substring `sub`, or `-1` if not found. |
| `in` | Checks if a substring exists within the string (returns `True`/`False`). |
| `zfill(width)` | Pads the string on the left with zeros until it reaches the given width. |
| `upper()` | Returns a copy of the string converted to uppercase. |
| `lower()` | Returns a copy of the string converted to lowercase. |
| `capitalize()` | Capitalizes the first character and lowercases the rest. |
| `isupper()` | Returns `True` if all cased characters are uppercase. |
| `islower()` | Returns `True` if all cased characters are lowercase. |
| `isnumeric()` | Returns `True` if all characters are numeric digits. |
| `isalpha()` | Returns `True` if all characters are alphabetic. |
| `split(sep)` | Splits the string into a list using a separator (whitespace by default). |
| `s[start:end]` | Slicing: returns a substring from index `start` to `end - 1`. |
| `s[start:end:step]` | Extended slice: allows skipping characters using `step` (e.g. reverse string using `[::-1]`). |



