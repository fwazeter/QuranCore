import os
from scripts.parse_quran import generate_master_file

if __name__ == "__main__":
    # Paths for the Quran XML file and the output JSON file
    xml_path = 'data/raw/quran-uthmani.xml'  # Input path for the Quran XML file
    output_path = 'data/surah_master.json'  # Output path for the master file

    if not os.path.exists(xml_path):
        print(f"❌ Error: The file '{xml_path}' does not exist.")
    else:
        print("🚀 Starting the process to generate the master file from the XML...")
        generate_master_file(xml_path, output_path)
        print("✅ Master file generation complete!")