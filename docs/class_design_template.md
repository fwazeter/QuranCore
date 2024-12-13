# **Class Design Template for Quran Analysis Project**

This document outlines the **consistent class design template** to be used across all classes in the Quran Analysis project. The goal is to maintain a high degree of **Separation of Concerns (SoC)**, **reusability**, and **encapsulation** while supporting **dependency injection** and **testability**.

---

## **1. Class Structure Overview**

Each class should follow this structure:

```python
class ClassName:
    """Class docstring to explain the purpose of this class."""

    def __init__(self, param1: type, param2: type, dependency_class: type):
        """Constructor method for initializing the class."""
        self.__param1 = param1  # Encapsulated attribute
        self.__param2 = param2  # Encapsulated attribute
        self.__dependency_class = dependency_class  # Injected dependency

    @classmethod
    def from_xml(cls, xml_element, dependency_class: type) -> 'ClassName':
        """Factory method to create a ClassName object from an XML element."""
        instance = cls(parsed_param1, parsed_param2, dependency_class)
        return instance

    @classmethod
    def from_dict(cls, data: dict, dependency_class: type) -> 'ClassName':
        """Factory method to create a ClassName object from a dictionary."""
        instance = cls(
            data.get('param1', default_value),
            data.get('param2', default_value),
            dependency_class
        )
        return instance

    def to_dict(self) -> dict:
        """Serialize the object to a dictionary."""
        return {
            'param1': self.__param1,
            'param2': self.__param2
        }

    # Getters
    def get_param1(self) -> type:
        """Get the value of param1."""
        return self.__param1

    def get_param2(self) -> type:
        """Get the value of param2."""
        return self.__param2

    # Setters
    def set_param1(self, value: type) -> None:
        """Set the value of param1."""
        self.__param1 = value

    def set_param2(self, value: type) -> None:
        """Set the value of param2."""
        self.__param2 = value
```

---

## **2. Naming Conventions**

- **Class Names**: Use **PascalCase** (e.g., `Surah`, `Ayah`, `Root`).
- **File Names**: Use **snake_case** (e.g., `surah.py`, `ayah.py`, `root.py`).
- **Encapsulation**: Private attributes must be prefixed with `__` (double underscores), e.g., `self.__id`.
- **Methods**: Use descriptive names that clearly convey the method's purpose.

---

## **3. Key Design Principles**

### **3.1. Separation of Concerns (SoC)**

- Each class should have a **single responsibility**.
- **Avoid combining multiple concerns** in one class (e.g., Surah handles Surah logic, while Ayah handles Ayah logic).

### **3.2. Encapsulation**

- **Use private attributes** to protect internal state (`__param1`).
- Provide **getters and setters** for controlled access to internal state.

### **3.3. Dependency Injection (DI)**

- **Inject dependencies via the constructor** rather than importing them.
- This allows dynamic injection of **mock objects** for testing.

### **3.4. Serialization**

- Each class must have **to_dict()** and **from_dict()** methods for JSON compatibility.
- Each class must also have **from_xml()** if it needs to parse XML data.

### **3.5. Avoid Circular Imports**

- Use **string-based type hints** like `-> 'Surah'` to avoid import errors.

---

## **4. Required Class Methods**

| **Method**          | **Purpose**                                 |
| ------------------- | ------------------------------------------- |
| **__init__()**      | Constructor to initialize attributes.       |
| **from_xml()**      | Create the object from an XML file.         |
| **from_dict()**     | Create the object from a Python dictionary. |
| **to_dict()**       | Export the object to a dictionary.          |
| **getters/setters** | Control access to internal attributes.      |

---

## **5. Commentation Guidelines**

To maintain consistency, readability, and professionalism, use the following commenting guidelines:

- **Class Docstrings**: Provide a brief description of the class, its purpose, and its main attributes.
- **Method Docstrings**: Clearly describe the purpose of the method, parameters, return values, and any side effects.
- **Inline Comments**: Use inline comments to explain **why** certain code is written in a particular way, not **what** the code does.
- **Block Comments**: Use block comments to separate logical sections of the code.

### **Example of Commentation**
```python
class Surah:
    """Represents a Surah in the Quran."""

    def __init__(self, id: int, name: str, revelation_order: int, total_ayahs: int, classification: str, ayah_class: type):
        """Constructor to initialize Surah attributes."""
        self.__id = id  # Unique identifier for the Surah
        self.__name = name  # Name of the Surah
        self.__revelation_order = revelation_order  # Revelation order of the Surah
        self.__total_ayahs = total_ayahs  # Total number of Ayahs in the Surah
        self.__classification = classification  # Meccan or Medinan classification
        self.__ayah_class = ayah_class  # Injected Ayah class dependency
        self.__ayahs = []  # List to hold Ayah objects
```

---

## **6. Design Prompts for GPT**

**Prompt 1**: *"Can you refactor the Surah class to follow the Quran Analysis Class Design Template?"*

**Prompt 2**: *"Can you implement a from_xml() and from_dict() method for the Ayah class?"*

**Prompt 3**: *"How can I inject the Ayah class into Surah without causing a circular import?"*

**Prompt 4**: *"Can you review my to_dict() and from_dict() methods to ensure consistency?"*

**Prompt 5**: *"Can you suggest improvements for ensuring Separation of Concerns (SoC) in my Word class?"*

---

## **7. Summary**
This document provides a **standardized class design template** for the Quran Analysis project. By following this structure, we ensure **maintainability, testability, and scalability**. Use this as a **guide for future class development** and reference it when adding new functionality.

