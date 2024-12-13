import os
from quran_engine.xml_loader import XMLLoader

# Step 1: Get the absolute path to the XML file
base_path = os.path.dirname(__file__)  # Directory of the current script
xml_path = os.path.join(base_path, 'data/raw/quran-uthmani.xml')

# Step 2: Load the XML file into the Quran object
try:
    print(f"Loading Quran from {xml_path}...")
    quran = XMLLoader.load_from_file(xml_path)
except Exception as e:
    print(f"Error loading Quran from XML: {e}")
    exit(1)

# Step 3: Print first Surah name and its first Ayah
try:
    first_surah = quran.get_surah(1)
    print(f"Surah Name: {first_surah.name}")
    print(f"First Ayah: {first_surah.ayahs[0].text_arabic}")
except Exception as e:
    print(f"Error accessing Surah or Ayah: {e}")

# Step 4: Export Quran to JSON
try:
    quran_json = quran.export_to_json()
    print(f"Exported Quran JSON (first 1000 characters):\n{quran_json[:1000]}")
except Exception as e:
    print(f"Error exporting Quran to JSON: {e}")

