# English — An Executable Pseudocode Language

> Write code that reads like structured English. Transpiled to Python and executed.

---

## Vision

Allow programmers to write code that reads like structured instructions while remaining easy to compile. English source code is transpiled into Python and then executed.

---

## Execution Pipeline

**Current**
```
hello.eng → output.py → Python Interpreter → Program Output
```

**Example**

*English source:*
```
Create variable age = 21
display age
```

*Generated Python:*
```python
age = 21
print(age)
```

*Result:*
```
21
```

---

**Future**
```
user.eng → Lexer → Parser → AST → Python Generator → output.py → Python Interpreter → Program Output
```

---

## Syntax Rules

- All block-opening statements end with a colon `:`
- Blocks are closed with `end` statements
- Indentation is used for readability
- Block termination is controlled by `end` statements, not indentation

```
if age > 18 :
    ...
end if

for loop i from 1 to 100 :
    ...
end loop

create function sum takes(a, b) :
    ...
end function
```

---

## Variables

**Mutable**
```
create variable age = 21
age = 22
```

**Immutable**
```
create constant pi = 3.1456
```
> Constants cannot be reassigned after declaration.

**Boolean** — follows Python convention: `True`, `False`, `None`

---

## Display & Return

```
display age
display "hello world"

return age
return "hello world"
```

> `display` is the primary output keyword.

---

## Operators

**Comparison**

| English Syntax | Meaning |
|---|---|
| `==` | Equal to (strict) |
| `=` | Equal to |
| `!=` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal |
| `>=` | Greater than or equal |

**Logical**

| Keyword | Meaning |
|---|---|
| `and` | Logical AND |
| `or` | Logical OR |
| `not` | Logical NOT |

**Arithmetic**

| Symbol | Operation |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Modulo |

---

## Arrays

```
create array nums = [1, 2, 3, 4]
create array nums = []
```

**Accessing elements**
```
display nums of i          → print(nums[i])
```

**Assigning elements**
```
nums of 0 = 100            → nums[0] = 100
```

**Length**
```
length(nums)               → len(nums)
```

**Operations**

| English | Python |
|---|---|
| `append 5 to nums` | `nums.append(5)` |
| `remove 5 from nums` | `nums.remove(5)` |
| `insert 10 at 2 in nums` | `nums.insert(2, 10)` |
| `pop nums` | `nums.pop()` |
| `clear nums` | `nums.clear()` |

---

## Conditional Statements

```
if age > 18 :
    display "adult"
else if age == 18 :
    display "just turned 18"
else :
    display "minor"
end if
```

---

## Loops

**For loop**
```
for loop i from 1 to 100 :
    display i
end loop
```

**While loop**
```
while loop age < 100 :
    age = age + 1
end loop
```

---

## Functions

**Declaration**
```
create function sum takes(a, b) :
    return a + b
end function
```

**Call**
```
sum(5, 10)
```

---

## Comments

```
// this is a comment
```

---

## Full Example

```
create variable age = 21
create constant limit = 18

create function check_age takes(a) :
    if a > limit :
        display "Access granted"
    else :
        display "Access denied"
    end if
end function

check_age(age)
```

*Generated Python:*
```python
age = 21
limit = 18

def check_age(a):
    if a > limit:
        print("Access granted")
    else:
        print("Access denied")

check_age(age)
```
