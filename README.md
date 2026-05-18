# Log Analyzer System (Case 5)

## 1. Project Description
A comprehensive, console-based Log Analyzer application built with Python. This project demonstrates advanced Python programming concepts, including Object-Oriented Programming (OOP), lazy evaluation, regular expressions, and higher-order functions. 

Key technical features include:
* **OOP & Polymorphism:** Custom string representations and strict status validation via property decorators.
* **Generators:** The parser reads log files line-by-line using `yield` to optimize memory usage and prevent memory overflow on massive files.
* **Higher-Order Functions:** Data filtering and transformations are purely handled by `map`, `filter`, and `lambda` expressions without redundant loops.
* **Unit Testing:** Comprehensive `unittest` coverage for models, parsers, and analytical components.

## 2. How to Run the Project
Follow these steps to run the application on your local machine:

**Step 1: Clone the repository**
```bash
git clone [https://github.com/yerasyppp/log-analyzer.git](https://github.com/yerasyppp/log-analyzer.git)
cd log-analyzer
```
**Step 2: Run the main application** 
```bash
python main.py
```
###### (Note: Use python3 main.py on macOS/Linux environments).

**Step 3: Run the Unit Tests (Optional but recommended)**
```bash
python -m unittest discover tests/
```

## 3. Team Members
### This project was developed collaboratively by a team of 4 members using Git Flow. Each member was responsible for a specific architectural module and its corresponding unit tests:

* **Yerassyl Irangait**: Coordinated the repository, managed Pull Requests, resolved merge conflicts, and developed the final interactive interface (main.py) to integrate all modules.

* **Ramazan Alzhanov**: Implemented the core data models using inheritance and encapsulation (models/log_entry.py) and wrote the associated tests (tests/test_models.py).

* **Ayazhan Yeslambek**: Developed the Regular Expression (regex) data extraction, optimized file reading using Generators, created the JSON export logic, and wrote the parsing tests (tests/test_parser.py).

* **Bayan Dauletkyzy** : Implemented the analytics logic (services/analyzer.py) utilizing Higher-Order Functions (filter, map, lambda) for efficient log processing, and wrote the analytics tests (tests/test_analyzer.py).
