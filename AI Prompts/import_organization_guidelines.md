# **Import Organization Guidelines for QuranCore Custom GPT**

Proper import organization is essential for maintainability, readability, and minimizing issues like circular imports. This document outlines best practices for organizing imports according to **PEP 8** and industry standards.

---

## **1. General Rules for Import Organization**

1. **Order Imports by Category**:
   - **Standard library imports** (e.g., `os`, `sys`, `datetime`, etc.)
   - **Third-party imports** (e.g., `numpy`, `pandas`, `requests`, etc.)
   - **Local imports** (e.g., `from quran_engine.quran import Quran`)

2. **Sort Imports Alphabetically**:
   - Within each category, sort imports **alphabetically** to make it easier to find and maintain.

3. **Avoid Unused Imports**:
   - Avoid importing unused modules to prevent linter errors.

4. **Use Explicit Imports**:
   - Instead of `from module import *`, always use **explicit imports** like `from quran_engine.quran import Quran`.

5. **Use Import Aliases When Necessary**:
   - Avoid long import names. For example, use `import pandas as pd`.

6. **Use Absolute Imports Over Relative Imports**:
   - Prefer absolute imports like `from quran_engine.quran import Quran`.

---

## **2. Recommended Import Order**

PEP 8 suggests dividing imports into three distinct groups, separated by a blank line:

```
1. Standard library imports
2. Third-party imports
3. Local application-specific imports
```

### **Example of Properly Ordered Imports**
```python
# 1. Standard library imports
import os
import sys
import unittest

# 2. Third-party imports
import numpy as np
import requests

# 3. Local application-specific imports
from quran_engine.quran import Quran
from quran_engine.surah import Surah
from quran_engine.ayah import Ayah
from quran_engine.word import Word
from quran_engine.root import Root
from quran_engine.gematria_engine import GematriaEngine
```

---

## **3. Local Import Guidelines**

If you’re importing local files, use **absolute imports** where possible.

### **Absolute Imports (Recommended)**
```python
# Absolute import from the main package
from quran_engine.quran import Quran
```

### **Relative Imports**
If **quran_engine/tests/** needs to import **quran_engine/quran.py**, you can use relative imports like this:
```python
# Relative import from the parent directory
from ..quran import Quran
```

**Best Practice**: Prefer **absolute imports** whenever possible.

---

## **4. Example of Properly Organized Imports in Tests**

Here’s an example of properly organized imports for a test file in **quran_engine/tests/test_quran.py**:

```python
"""
Test File for Quran Class
-------------------------
This test file ensures the proper functionality of the Quran class, including:
- Adding Surahs to the Quran.
- Calculating total word counts and total gematric sums.
- Exporting the entire Quran to JSON.
"""

# 1. Standard library imports
import unittest
import json

# 2. Third-party imports (none in this case)

# 3. Local application-specific imports
from quran_engine.quran import Quran
from quran_engine.surah import Surah
from quran_engine.ayah import Ayah
from quran_engine.word import Word
from quran_engine.root import Root

class TestQuran(unittest.TestCase):

    def setUp(self):
        """Set up the test environment for each test case."""
        self.quran = Quran()
        self.surah = Surah(1, "Al-Fatiha", 5, 7, "Meccan")
        self.quran.add_surah(self.surah)

    def test_total_word_count(self):
        """Test that total word count is accurate."""
        self.assertEqual(self.quran.total_word_count(), 0)

if __name__ == '__main__':
    unittest.main()
```

---

## **5. Managing `__init__.py`**

The **`__init__.py`** file tells Python to treat the directory as a **package**. It can also be used to expose certain classes or modules.

**Minimal `__init__.py`** (can be empty):
```python
# Empty file to mark quran_engine as a package
```

**Explicit Export `__init__.py`**:
```python
from .quran import Quran
from .surah import Surah
from .ayah import Ayah
from .word import Word
from .root import Root
from .gematria_engine import GematriaEngine

__all__ = ['Quran', 'Surah', 'Ayah', 'Word', 'Root', 'GematriaEngine']
```

This allows you to import directly like this:
```python
from quran_engine import Quran, Surah
```

---

## **6. Automatic Import Sorting with isort**

Instead of sorting imports manually, use **isort**.

### **Install isort**
```bash
pip install isort
```

### **Sort All Files in QuranCore**
```bash
isort .
```

This will sort all imports in **all files** under the **current directory**.

---

## **7. Avoiding Common Issues**

### **Common Issues and Solutions**
| **Issue**                     | **Cause**                                     | **Solution**                                              |
|------------------------------|-----------------------------------------------|----------------------------------------------------------|
| `ModuleNotFoundError`         | No `__init__.py` in **quran_engine**          | Add `__init__.py` to **quran_engine/**                     |
| **Relative Import Error**     | Used relative import without `__init__.py`    | Add **`__init__.py`** to **quran_engine/tests/**           |
| **ImportError (circular)**    | Import loop between files                     | Use `if TYPE_CHECKING:` for type hints to avoid loops      |
| **Cannot import name**        | Misspelled class or filename                  | Check for typos in class names and filenames               |

---

## **Summary**
1. **Order imports into 3 groups**: standard library, third-party, and local imports.
2. **Use absolute imports** whenever possible.
3. **Use isort** to automatically sort imports.
4. **Avoid relative imports** (`from ..quran import Quran`) unless absolutely necessary.
5. **Use `__init__.py`** to make packages importable and export key classes.

---

If you'd like, I can **create all the `__init__.py` files** and ensure that **all imports are properly organized** according to this document. Let me know if you'd like that to be done automatically.

