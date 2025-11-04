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



## Common Python List Methods

| Method | Description |
|--------|-------------|
| `append(x)` | Adds an element `x` to the end of the list. |
| `extend(iterable)` | Adds all elements from another iterable (like a list or tuple) to the end. |
| `insert(i, x)` | Inserts an element `x` at position `i`. |
| `remove(x)` | Removes the first occurrence of `x` from the list. |
| `pop(i)` | Removes and returns the element at index `i` (last item by default). |
| `clear()` | Removes all items from the list. |
| `index(x)` | Returns the index of the first occurrence of `x`. |
| `count(x)` | Returns the number of times `x` appears in the list. |
| `sort(reverse=False, key=None)` | Sorts the list in ascending order (by default). |
| `reverse()` | Reverses the order of elements in the list. |
| `copy()` | Returns a shallow copy of the list. |

---

### List Operations & Slicing

| Operation / Syntax | Description |
|--------------------|-------------|
| `len(lst)` | Returns the number of elements in the list. |
| `x in lst` | Checks if `x` is an element of the list. |
| `lst[start:end]` | Returns a sublist from `start` to `end - 1`. |
| `lst[start:end:step]` | Returns a sliced list, skipping elements by `step` (e.g. reverse with `[::-1]`). |
| `+` | Concatenates two lists. |
| `*` | Repeats a list multiple times (e.g. `[1, 2] * 3 → [1, 2, 1, 2, 1, 2]`). |

> 💡 **Tip:** Lists are mutable, meaning their contents can be changed in place.


## Common Python Tuple Methods & Operations

| Method / Operation | Description |
|--------------------|-------------|
| `count(x)` | Returns the number of times `x` appears in the tuple. |
| `index(x)` | Returns the index of the first occurrence of `x`. |


---

### Tuple Operations & Features

| Operation / Syntax | Description |
|--------------------|-------------|
| `len(tpl)` | Returns the number of elements in the tuple. |
| `x in tpl` | Checks if `x` is an element of the tuple. |
| `tpl[start:end]` | Returns a subtuple from `start` to `end - 1`. |
| `tpl[start:end:step]` | Returns a sliced tuple (e.g. reversed with `[::-1]`). |
| `+` | Concatenates two tuples. |
| `*` | Repeats the tuple multiple times (e.g. `(1, 2) * 3 → (1, 2, 1, 2, 1, 2)`). |
| `tuple(iterable)` | Converts an iterable (like a list or string) into a tuple. |

> 💡 **Note:** Tuples are **immutable**, meaning their elements cannot be changed after creation.

## Common Python Set Methods & Operations

| Method | Description |
|--------|-------------|
| `add(x)` | Adds an element `x` to the set. |
| `update(iterable)` | Adds multiple elements from another iterable (like a list or set). |
| `remove(x)` | Removes element `x` from the set; raises an error if not found. |
| `discard(x)` | Removes element `x` if it exists — no error if it doesn’t. |
| `pop()` | Removes and returns a random element from the set. |
| `clear()` | Removes all elements from the set. |
| `copy()` | Returns a shallow copy of the set. |
| `union(other, ...)` or `|` | Returns a new set with elements from both sets. |
| `intersection(other, ...)` or `&` | Returns a new set with elements common to both sets. |
| `difference(other, ...)` or `-` | Returns a new set with elements in this set but not the other(s). |
| `symmetric_difference(other)` or `^` | Returns a new set with elements in either set, but not both. |
| `issubset(other)` | Returns `True` if all elements of this set are contained in `other`. |
| `issuperset(other)` | Returns `True` if this set contains all elements of `other`. |
| `isdisjoint(other)` | Returns `True` if the sets have no elements in common. |

---

### Set Operations & Features

| Operation / Syntax | Description |
|--------------------|-------------|
| `len(s)` | Returns the number of elements in the set. |
| `x in s` | Checks if `x` is an element of the set. |
| `set(iterable)` | Creates a set from an iterable (e.g. list or string). |
| `frozenset(iterable)` | Creates an **immutable** version of a set. |

> 💡 **Note:** Sets are **unordered** and **do not allow duplicates**.


## Common Python Dictionary Methods & Operations

| Method | Description |
|--------|-------------|
| `clear()` | Removes all items from the dictionary. |
| `copy()` | Returns a shallow copy of the dictionary. |
| `fromkeys(keys, value)` | Creates a new dictionary with given keys, all set to the same value. |
| `get(key, default)` | Returns the value for `key` if it exists, otherwise returns `default`. |
| `items()` | Returns a view object with all key-value pairs as tuples. |
| `keys()` | Returns a view object with all keys. |
| `values()` | Returns a view object with all values. |
| `pop(key, default)` | Removes the specified key and returns its value. If not found, returns `default` (if given). |
| `popitem()` | Removes and returns the last inserted key-value pair. |
| `setdefault(key, default)` | Returns the value of `key`. If not found, inserts `key` with `default` value. |
| `update(other_dict)` | Updates the dictionary with key-value pairs from another dictionary or iterable. |

---

### Dictionary Operations & Features

| Operation / Syntax | Description |
|--------------------|-------------|
| `len(d)` | Returns the number of key-value pairs in the dictionary. |
| `key in d` | Checks if the given key exists in the dictionary. |
| `del d[key]` | Deletes the key-value pair with the given key. |
| `d[key] = value` | Adds or updates a key-value pair. |
| `{key: value, ...}` | Creates a dictionary literal. |
| `dict(iterable)` | Creates a dictionary from a sequence of key-value pairs or another mapping. |

> 💡 **Note:** Dictionaries store data as **key–value pairs** and are **unordered** (insertion order is preserved since Python 3.7+).



## Python OOP (Object-Oriented Programming) – Key Syntax & Magic Methods

### 🧱 Class Basics

| Syntax / Keyword | Description |
|------------------|-------------|
| `class ClassName:` | Defines a new class. |
| `__init__(self, ...)` | **Constructor:** Called automatically when an object is created. Used to initialize attributes. |
| `self` | Refers to the current instance of the class. |
| `object = ClassName()` | Creates a new instance (object) of the class. |
| `__del__(self)` | **Destructor:** Called when the object is about to be destroyed. |
| `__repr__(self)` | Returns an official string representation of the object (for developers). |
| `__str__(self)` | Returns a readable string representation (for users, e.g. in `print()`). |

---

### 🧩 Magic (Dunder) Methods – Common Operations

| Method | Trigger / Purpose |
|--------|-------------------|
| `__len__(self)` | Called by `len(obj)` to return the object’s length. |
| `__getitem__(self, key)` | Defines behavior for indexing (e.g. `obj[key]`). |
| `__setitem__(self, key, value)` | Defines behavior for assigning to an index (e.g. `obj[key] = value`). |
| `__delitem__(self, key)` | Defines behavior for deleting an item (e.g. `del obj[key]`). |
| `__iter__(self)` | Returns an iterator for the object (used in loops). |
| `__next__(self)` | Returns the next item in iteration. |
| `__contains__(self, item)` | Called when using the `in` keyword (`item in obj`). |

---

### ➕ Magic Methods for Operators

| Method | Trigger / Example |
|--------|-------------------|
| `__add__(self, other)` | `obj1 + obj2` |
| `__sub__(self, other)` | `obj1 - obj2` |
| `__mul__(self, other)` | `obj1 * obj2` |
| `__truediv__(self, other)` | `obj1 / obj2` |
| `__floordiv__(self, other)` | `obj1 // obj2` |
| `__mod__(self, other)` | `obj1 % obj2` |
| `__pow__(self, other)` | `obj1 ** obj2` |
| `__eq__(self, other)` | `obj1 == obj2` |
| `__ne__(self, other)` | `obj1 != obj2` |
| `__lt__(self, other)` | `obj1 < obj2` |
| `__le__(self, other)` | `obj1 <= obj2` |
| `__gt__(self, other)` | `obj1 > obj2` |
| `__ge__(self, other)` | `obj1 >= obj2` |

---

### 🧠 Class Features

| Concept / Keyword | Description |
|-------------------|-------------|
| `@classmethod` | Defines a method that receives the **class** as the first argument (`cls`) instead of `self`. |
| `@staticmethod` | Defines a method that doesn’t need `self` or `cls`. Works like a regular function inside the class. |
| `@property` | Turns a method into a “getter” (can be accessed like an attribute). |
| `@<property>.setter` | Defines a setter for a property. |
| `@<property>.deleter` | Defines a deleter for a property. |
| `isinstance(obj, Class)` | Checks if an object is an instance of a class. |
| `issubclass(Sub, Base)` | Checks if a class inherits from another class. |
| `super()` | Calls a method from the parent class. |
| `__class__` | Returns the class of the current instance. |

---

### 🧬 Inheritance & Polymorphism


| Concept                  | Syntax / Keyword                          | Description                                    |
| ------------------------ | ----------------------------------------- | ---------------------------------------------- |
| **Inheritance**          | `class Child(Parent):`                    | Child class inherits attributes & methods.     |
| **Super Constructor**    | `super().__init__()`                      | Calls parent’s constructor.                    |
| **Overriding**           | Redefine a parent method                  | Change inherited method behavior.              |
| **Multiple Inheritance** | `class C(A, B):`                          | Inherit from multiple classes.                 |
| **Abstract Class**       | `class MyClass(ABC):` + `@abstractmethod` | Defines base behavior; cannot be instantiated. |


---