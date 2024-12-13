import os
import json
import xml.etree.ElementTree as ET
from scripts.Quran import Quran


def parse_quran_xml(xml_path: str) -> dict:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    surahs_data = {}

    for sura in root.findall('sura'):
        surah_id = int(sura.get('index'))
        surah_name = sura.get('name')

        surah_entry = {
            'SurahID': surah_id,
            'ArabicTitle': surah_name,
            'EnglishTitle': '',
            'RevelationOrder': 0,
            'Grouping': '',
            'Ayahs': []
        }

        for ayah in sura.findall('aya'):
            ayah_index = int(ayah.get('index'))
            ayah_text = ayah.get('text')

            # Call the Quran analyze_ayah method
            quran = Quran()  # No path required
            ayah_data = quran.analyze_ayah(ayah_text)
            ayah_data['AyahID'] = ayah_index

            surah_entry['Ayahs'].append(ayah_data)

        surahs_data[str(surah_id)] = surah_entry

    return surahs_data


def write_master_file(output_path: str, data: dict) -> None:
    """
    Writes the master JSON file for the Quran data.
    Args:
        output_path (str): The path where the master JSON file will be saved.
        data (dict): The Quran data to be written.
    """
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def generate_master_file(xml_path: str, output_path: str) -> None:
    """
    Generates a master file for the Quran using the source XML data.
    Args:
        xml_path (str): The path to the source Quran XML file.
        output_path (str): The path to save the master JSON file.
    """
    print(f"Parsing Quran from {xml_path}...")
    surahs_data = parse_quran_xml(xml_path)
    print(f"Successfully parsed {len(surahs_data)} surahs.")

    write_master_file(output_path, surahs_data)
    print(f"Master file saved as {output_path}.")



