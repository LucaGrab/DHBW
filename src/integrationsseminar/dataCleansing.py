import json


def load_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def count_duplicates(data):
    id_set = set()
    duplicate_count = 0

    for item in data:
        entry_id = item.get("id")
        if entry_id in id_set:
            duplicate_count += 1
        else:
            id_set.add(entry_id)

    total_entries = len(data)
    return total_entries, duplicate_count


def save_data_without_duplicates(data, output_file):
    id_set = set()
    unique_data = []

    for item in data:
        entry_id = item.get("id")
        if entry_id not in id_set:
            id_set.add(entry_id)
            unique_data.append(item)

    with open(output_file, "w") as file:
        json.dump(unique_data, file, indent=2)


if __name__ == "__main__":
    # Beispiel-Pfad zur JSON-Datei
    file_path = "bad_escooter_data.json"

    # Lade die JSON-Daten aus der Datei
    data = load_json_file(file_path)

    # Zähle Gesamteinträge und Duplikate
    total_entries, duplicate_count = count_duplicates(data)

    # Berechne den Prozentsatz der Duplikate
    percentage_duplicates = (duplicate_count / total_entries) * 100

    # Zeige die Ergebnisse an
    print(f"Gesamtanzahl der Einträge: {total_entries}")
    print(f"Anzahl der Duplikate: {duplicate_count}")
    print(f"Prozentsatz der Duplikate: {percentage_duplicates:.2f}%")

    # Annahme: 'data' ist bereits geladen und 'output_file' ist der Pfad zur Ausgabedatei
    output_file = "cleanedData.json"
    save_data_without_duplicates(data, output_file)

    # Lade die JSON-Daten aus der Datei
    data = load_json_file(output_file)

    # Zähle Gesamteinträge und Duplikate
    total_entries, duplicate_count = count_duplicates(data)

    # Berechne den Prozentsatz der Duplikate
    percentage_duplicates = (duplicate_count / total_entries) * 100

    # Zeige die Ergebnisse an
    print(f"Gesamtanzahl der Einträge: {total_entries}")
    print(f"Anzahl der Duplikate: {duplicate_count}")
    print(f"Prozentsatz der Duplikate: {percentage_duplicates:.2f}%")
