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

### 📁 [Lab 03](./Lab-03) - Graph Algorithms & Traveling Salesperson Problem (TSP)
This section explores graph representations, shortest path lookups, and algorithmic approaches to NP-hard optimization problems.
* **Graph Representation (`graph.py`)**: Core data structures used to model and navigate custom graph topologies.
* **Exact TSP Solver (`tsp_exact.py`)**: An implementation of an exact, brute-force/backtracking algorithm designed to find the absolute optimal Hamiltonian cycle for the Traveling Salesperson Problem.
* **Approximation TSP Solver (`tsp_approx.py`)**: A heuristic approach implementing an efficient approximation algorithm to solve TSP for larger datasets where exact computation becomes computationally intractable.
* **Bidirectional Search (`bidirectional.py`)**: An optimized graph traversal algorithm executing simultaneous forward and backward searches to establish the shortest path between nodes with significantly reduced state-space exploration.

### 📁 [Lab 04](./Lab-04) - Priority Queues, Data Compression & String Metrics
This section explores tree-based data structures, optimal prefix coding for lossless compression, and dynamic programming for string similarity.
* **Custom Heap (`heap.py`)**: Implementation of a binary heap data structure, serving as an efficient priority queue.
* **Huffman Coding (`huffman.py`)**: Implementation of the Huffman compression algorithm. It utilizes the custom heap to build a frequency-based binary tree, generating optimal prefix codes for lossless data compression.
* **Spell Checker & String Distances (`spell_checker.py`, `distances.py`)**: A spell-checking utility that processes a text dictionary (`words_alpha.txt`) and calculates string metrics (e.g., Edit/Levenshtein distance) to dynamically find and suggest the closest valid word matches for misspelled inputs.

---

## Technical Highlights
* **Language**: Python 3.x
* **Core Focus**: 
  * Understanding the underlying mechanics of foundational data structures (Stacks, Linked Lists, Priority Queues/Heaps, Graphs).
  * Algorithmic application of data structures (Lossless compression, shortest path heuristics, dynamic programming).
  * Strict adherence to constraints (e.g., custom heap construction, manual multidimensional array transformations).
