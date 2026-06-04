---
title: Zenthon
layout: default
---

# Zenthon

Zenthon is a high-level programming language for ZenOS. It is designed to feel readable like Python, structured like JavaScript, and lightweight like Lua.

## Design Goals

- Beginner-friendly syntax
- Curly-brace blocks instead of indentation rules
- Dynamic typing with no type declarations
- Simple built-in data structures
- No low-level memory management, pointers, or manual allocation

## File Extension

Zenthon source files use the `.zth` extension.

## Core Style

- Blocks use `{` and `}`
- Statements usually live one per line
- Semicolons are not used
- Variables are created with `=`
- Functions are declared with `function`

## Basic Example

```zenthon
name = "ZenOS"
number = 9

print("Hello, " + name + "!")
print("Number is " + number)
```

## Values

Zenthon is dynamically typed. A variable can hold any kind of value and can later be reassigned to a different kind of value.

Supported core values:

- Numbers: `1`, `9`, `3.14`
- Strings: `"hello"`
- Booleans: `true`, `false`
- Empty value: `null`
- Lists: `[1, 2, 3]`
- Dictionaries: `{ "name": "ZenOS" }`

## Variables

Assignment uses `=`.

```zenthon
language = "Zenthon"
score = 9
score = score + 1
```

## Strings

Strings use double quotes.

```zenthon
message = "hello"
print(message)
```

`+` joins strings. If either side is a string, the other side is automatically converted into a string.

```zenthon
print("I like " + "sushi")
print("Number is " + 9)
```

## Comments

Single-line comments:

```zenthon
// This is a comment
## This is also a comment
```

Multi-line comments:

```zenthon
#/
This is a multi-line comment.
It can span multiple lines.
/# 
```

## Functions

Functions are declared with `function name(params) { ... }`.

```zenthon
function greet(name) {
    print("Hello, " + name + "!")
}

greet("friend")
```

Functions can return values with `return`.

```zenthon
function add(a, b) {
    return a + b
}

total = add(4, 5)
print("Total: " + total)
```

## Conditionals

Zenthon uses `=` for equality comparison inside conditions.

```zenthon
if x = 1 then {
    print("x is one")
} else {
    print("x is not one")
}
```

`else if` chains are allowed:

```zenthon
if score >= 90 then {
    print("A")
} else if score >= 80 then {
    print("B")
} else {
    print("Keep going")
}
```

## Comparison and Assignment Rules

Zenthon uses `=` in two different ways:

- In statement position, `=` assigns a value
- Inside a condition or comparison expression, `=` checks equality

Examples:

```zenthon
name = "sushi"            // assignment

if name = "sushi" then {  // comparison
    print("Correct")
}
```

To keep the language easy to read, assignment is a statement, not an expression. That means you cannot hide an assignment inside an `if` or `while` condition.

## Loops

### `for`

The numeric `for` loop counts from a start value to an end value, inclusive.

```zenthon
for i = 1 to 5 {
    print("Loop #" + i)
}
```

### `while`

```zenthon
count = 3

while count > 0 {
    print("Countdown: " + count)
    count = count - 1
}
```

## Operators

Arithmetic operators:

- `+`
- `-`
- `*`
- `/`
- `%`

Comparison operators:

- `=`
- `!=`
- `<`
- `>`
- `<=`
- `>=`

Logical operators:

- `and`
- `or`
- `not`

Parentheses can be used to make intent clear:

```zenthon
if (score > 5 and not finished) or admin then {
    print("Access granted")
}
```

## Data Structures

### Lists

Lists use square brackets.

```zenthon
numbers = [1, 2, 3]
print(numbers[0])
```

List indexing is zero-based.

### Dictionaries

Dictionaries use curly braces with key-value pairs.

```zenthon
player = {
    "name": "Max",
    "score": 9
}

print(player["name"])
```

Dictionary keys are string-based in the base language design.

## Blocks vs Dictionaries

Zenthon uses `{}` for both blocks and dictionary literals.

The meaning is determined by context:

- After `function`, `if ... then`, `else`, `for`, or `while`, `{}` starts a code block
- In expression position, `{}` creates a dictionary

Examples:

```zenthon
function demo() {
    info = { "kind": "dictionary" }
    print(info["kind"])
}
```

## Standard Library

### `print(value)`

Writes a readable version of a value to the console.

### `len(value)`

Returns:

- string length for strings
- item count for lists
- key count for dictionaries

### `range()`

Creates a list of numbers.

```zenthon
range(3)        // [0, 1, 2, 3]
range(2, 5)     // [2, 3, 4, 5]
```

Zenthon ranges are inclusive to match `for i = start to end`.

### `str(value)`

Converts a value into a string.

### `int(value)`

Converts a string or number into an integer. Decimal values are truncated toward zero.

## Complete Syntax Walkthrough

```zenthon
// Variables
favorite = "sushi"
number = 3

// Function
function awesome() {
    if favorite = "sushi" then {
        print(favorite + " is the best!")
    } else {
        print("Maybe try noodles too.")
    }

    for i = 1 to number {
        print("Loop #" + i)
    }

    while number > 0 {
        print("Countdown: " + number)
        number = number - 1
    }
}

awesome()
```

## Example Programs

The zenOS repository includes sample Zenthon programs in `examples/zenthon/`:

- `hello.zth`
- `control_flow.zth`
- `collections.zth`
- `fizzbuzz.zth`

## Summary

Zenthon is meant to be easy to learn:

- readable variable assignment
- explicit curly-brace blocks
- simple `function` definitions
- inclusive `for` loops
- beginner-friendly string concatenation
- built-in lists and dictionaries

It is intentionally small, expressive, and friendly for ZenOS users who want to write clear programs without dealing with low-level complexity.
