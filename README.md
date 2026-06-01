# Algorithms and Data Structures in Python

This repository contains university lab assignments, algorithm implementations, and custom data structure exercises developed during the Algorithms and Data Structures (ADS) course. 

## Repository Structure

The project is organized by laboratory sessions, with each folder focusing on specific algorithmic paradigms or data structures:

### 📁 [Lab 01](./Lab-01) - Fundamental Data Structures (Stack & Linked List)
This section focuses on implementing fundamental data structures from scratch without relying on Python's built-in modules.
* **Task 1: Stack & Reverse Polish Notation (RPN) (`Lab1Task1.py`)**
  * Custom implementation of an array-based stack (`push`, `pop`, `isempty`, `top`).
  * Algorithm to convert infix mathematical expressions to postfix notation (RPN), handling a custom/reversed operator precedence.
  * An evaluation engine to compute the final value of the converted postfix expressions.
* **Task 2: Singly Linked List & Palindrome Checker (`Lab1Task2.py`)**
  * Custom implementation of a singly linked list and parsing strings into individual nodes.
  * Integration with the previously built stack to verify if the character sequence forms a palindrome.

### 📁 [Lab 02](./Lab-02) - Image Processing & 2D Array Manipulation
This section focuses on low-level image processing and multidimensional array manipulation without relying on high-level computer vision libraries.
* **Task 1: Histogram Equalization (`histogram_equalization.py`)**
  * Enhancing image contrast by computing the probability mass function (PMF) and cumulative distribution function (CDF) to redistribute pixel intensities across the spectrum.
* **Task 2: Image Thresholding (`thresholding.py`)**
  * Implementing a binarization algorithm that converts grayscale images into black-and-white based on a dynamic or static pixel intensity threshold.
* **Task 3: Mean Filter (`mean_filter.py`)**
  * Applying a spatial low-pass filter (convolution matrix) for image smoothing and noise reduction, including custom boundary handling for edge pixels.

---

## Technical Highlights
* **Language**: Python 3.x
* **Core Focus**: 
  * Understanding the underlying mechanics of foundational data structures (Stacks, Singly Linked Lists).
  * Low-level multidimensional array transformations and image processing.
  * Algorithmic application of data structures (RPN parsing, mathematical evaluation, string validation).
  * Strict adherence to constraints (e.g., no usage of standard library equivalents like `list.pop()`, manual pixel manipulation).
