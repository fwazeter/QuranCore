# **Quran Analysis System Documentation**

This document serves as a comprehensive guide to the **Quran Analysis System**. It outlines its **usage**, **class interactions**, and **future next steps** to improve the system. This system is designed with **DRY, SOC, and OOP best practices** to ensure **modular, maintainable, and ready for porting to other languages** like **Rust, Java, or TypeScript**.

---

## **Table of Contents**
1. [Overview](#overview)
2. [Usage Examples](#usage-examples)
3. [Class Interactions](#class-interactions)
4. [Next Steps for Development](#next-steps-for-development)
5. [Future Enhancements](#future-enhancements)

---

## **1. Overview**
The Quran Analysis System is an **object-oriented system** for managing, analyzing, and exporting data related to the Quran. It enables **gematric analysis**, **NLP integration**, **thematic tagging**, and **data consolidation** for use in **SQL, RDF, Neo4j**, and **embedding-based AI models**.

### **Class Structure**
```
Quran ➞ Surah ➞ Ayah ➞ Word ➞ Root ➞ Concept/Tag
```

- **Quran**: The main entry point for accessing, querying, and analyzing Quranic data.
- **Surah**: Represents a Surah (chapter) of the Quran, containing multiple **Ayahs**.
- **Ayah**: Represents a verse, containing multiple **Words**.
- **Word**: Represents a single word, with its associated **Root**, **Gematria**, and **Grammar**.
- **Root**: Tracks the root words linked to **Words**.
- **Concept/Tag**: Links concepts (like **"Mercy"**) to Ayahs, Words, and Roots for thematic analysis.

---

## **2. Usage Examples**

These usage examples demonstrate how to interact with the system, calculate totals, and query concepts and themes.

---

### **1. Create the Quran and Add Surahs, Ayahs, and Words**
```python
from quran_analysis import Quran, Surah, Ayah, Word, Root, GematriaEngine

# Step 1: Create a Quran instance
quran = Quran()

# Step 2: Create a Surah (e.g., Surah Al-Fatiha)
surah_1 = Surah(1, "Al-Fatiha", 5, 7, "Meccan")
quran.add_surah(surah_1)

# Step 3: Add an Ayah to Surah 1
ayah_1 = Ayah(1, 1, "بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيمِ", "بسم الله الرحمن الرحيم")
surah_1.add_ayah(ayah_1)

# Step 4: Add Words to the Ayah
word_1 = Word(1, "بِسْمِ", Root(1, "سمو", "Exaltation"), "Noun")
word_2 = Word(2, "اللهِ", Root(2, "له", "Divine"), "Proper Noun")
ayah_1.add_word(word_1)
ayah_1.add_word(word_2)
```

---

### **2. Calculate Total Word Count for the Entire Quran**
```python
total_words = quran.total_word_count()
print(f"Total Words in the Quran: {total_words}")
```

**Output**
```
Total Words in the Quran: 2
```

---

### **3. Calculate the Total Gematric Sum of All Words**
```python
total_gematria = quran.total_gematric_sum()
print(f"Total Gematric Sum: {total_gematria}")
```

**Output**
```
Total Gematric Sum: 168
```

---

### **4. Export the Entire Quran to JSON**
```python
quran_json = quran.export_to_json()
print(quran_json)
```

**Output (example)**
```json
{
  "surahs": [
    {
      "id": 1,
      "name": "Al-Fatiha",
      "revelation_order": 5,
      "total_ayahs": 7,
      "classification": "Meccan",
      "ayahs": [
        {
          "id": 1,
          "position": 1,
          "text_arabic": "بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيمِ",
          "words": [
            {"id": 1, "text_arabic": "بِسْمِ", "gematric_value": 102},
            {"id": 2, "text_arabic": "اللهِ", "gematric_value": 66}
          ]
        }
      ]
    }
  ]
}
```

---

## **3. Class Interactions**

The following diagram shows the interaction between the classes and how they relate to each other.

```
Quran ➞ Surah ➞ Ayah ➞ Word ➞ Root ➞ Concept/Tag
```

---

## **4. Next Steps for Development**

- **Export to SQL**: Export to SQL database to allow large-scale queries.
- **Export to RDF**: Export Quran data as **RDF triples** for use in **SPARQL queries**.
- **Port to Rust**: Convert the Python structure to **Rust structs and traits**.
- **Query Enhancements**: Add **query filters** like "find all Ayahs related to **Mercy**".

---

## **5. Future Enhancements**

| **Feature**           | **Description**                                 | **Priority**  |
|----------------------|-------------------------------------------------|---------------|
| **Port to Rust**       | Port all classes to Rust for better performance.| 🔥 High       |
| **SQL Exporter**       | Export to SQL to enable joins, queries, and views.| 🔥 High      |
| **Conceptual Linking** | Link **themes** to Ayahs, Roots, and Concepts.  | ⚡ Medium     |
| **Visualization**      | Add data visualizations of roots, themes, and links.| ⚡ Medium  |

