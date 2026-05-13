# Valid Parentheses

## Overview
This project provides an efficient solution to the **Valid Parentheses** problem using a stack-based approach. The algorithm ensures that every opening bracket has a corresponding closing bracket of the same type and that brackets are closed in the correct order.

## Problem Statement
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Implementation Details
The solution is implemented in `main.py` using the following logic:
- **Data Structure**: A `list` is used as a stack to maintain the order of opening brackets.
- **Mapping**: A dictionary maps closing brackets to their corresponding opening brackets for quick lookup.
- **Process**:
  - Iterate through each character in the string.
  - If it's an opening bracket, push it onto the stack.
  - If it's a closing bracket, check if the stack is empty or if the top of the stack matches the expected opening bracket.
  - Finally, check if the stack is empty to ensure all brackets were closed.

## Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of the string. We traverse the string once.
- **Space Complexity**: $O(n)$, in the worst case where all characters are opening brackets.

## Usage
```python
from main import Solution

sol = Solution()
print(sol.isValid("()[]{}")) # Output: True
print(sol.isValid("(]"))     # Output: False
```
