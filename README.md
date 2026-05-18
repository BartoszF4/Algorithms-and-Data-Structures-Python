# Algorithms and Data Structures in Python

This repository contains university lab assignments, algorithm implementations, and custom data structure exercises developed during the Algorithms and Data Structures (ADS) course. 

## Repository Structure

The project is organized by laboratory sessions, with each folder focusing on specific algorithmic paradigms or data structures:

### 📁 [Lab 01](./Lab-01) - Fundamental Data Structures (Stack & Linked List)
This section focuses on implementing fundamental data structures from scratch without relying on Python's built-in modules.

* **Task 1: Stack & Reverse Polish Notation (RPN) (`Lab1Task1.py`)**
  * Custom implementation of an array-based stack (`push`, `pop`, `isempty`, `top`).
  * Algorithm to convert infix mathematical expressions to postfix notation (RPN), handling a custom/reversed operator precedence (where addition/subtraction are prioritized over multiplication/division).
  * An evaluation engine to compute the final value of the converted postfix expressions.
  
* **Task 2: Singly Linked List & Palindrome Checker (`Lab1Task2.py`)**
  * Custom implementation of a singly linked list.
  * Algorithm that parses strings of characters into individual list nodes.
  * Integration with the previously built stack structure to verify if the character sequence forms a palindrome.

---

## Technical Highlights
* **Language**: Python 3.x
* **Core Focus**: 
  * Understanding the underlying mechanics of foundational data structures (Stacks, Singly Linked Lists).
  * Algorithmic application of data structures (RPN parsing, mathematical evaluation, string validation).
  * Strict adherence to constraints (no usage of standard library equivalents like `list.pop()` or `collections.deque`).
