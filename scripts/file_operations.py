import json
import os

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_json(file_path, data):
    """
    Writes data to a JSON file using atomic write to ensure data integrity.
    """
    temp_path = f"{file_path}.tmp"
    with open(temp_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    os.replace(temp_path, file_path)


def write_summary_totals(output_dir, surahs_data):
    total_numbered_verses = sum(surah['TotalNumberedVerses'] for surah in surahs_data)
    total_verses = sum(surah['TotalVerses'] for surah in surahs_data)
    total_words = sum(ayah['TotalWords'] for surah in surahs_data for ayah in surah['Ayahs'])
    total_gematric_values = sum(
        sum(ayah['GematricValues']) for surah in surahs_data for ayah in surah['Ayahs'])

    summary_totals = {
        "TotalNumberedVerses": total_numbered_verses,
        "TotalVerses": total_verses,
        "TotalWords": total_words,
        "TotalGematricValue": total_gematric_values
    }

    write_json(os.path.join(output_dir, 'summary_totals.json'), summary_totals)


def list_verses_divisible_by_19(surahs_data, output_file):
    """
    Identifies all Ayahs whose TotalGematricValue is divisible by 19 and outputs the results to a JSON file.

    Args:
        surahs_data (list): List of all Surah data.
        output_file (str): Path to the output JSON file to save the results.
    """
    divisible_ayahs = []
    for surah in surahs_data:
        for ayah in surah['Ayahs']:
            if ayah['TotalGematricValue'] % 19 == 0:
                divisible_ayahs.append({
                    "SurahID": surah['SurahID'],
                    "AyahID": ayah['AyahID'],
                    "TotalGematricValue": ayah['TotalGematricValue']
                })

    write_json(output_file, divisible_ayahs)