import requests
import time
import json
import pandas as pd

def send_rest_request():
    print("Sende Anfrage...")
    response = requests.get("https://platform.tier-services.io/v2/vehicle?zoneId=LEIPZIG",
                            headers={"X-API-Key": "bpEUTJEBTf74oGRWxaIcW7aeZMzDDODe1yBoSxi2"})
    return response

anzahl_anfragen = 3
zeitversatz = 10 

for i in range(anzahl_anfragen):
    response = send_rest_request()
    
    if response.status_code == 200:
        data = response.json()
        filename = f"leipzig_data_{i + 1}.json"
        with open(filename, "w") as file:
            json.dump(data, file)
        print(f"Daten erfolgreich in {filename} gespeichert.")
        with open(filename, "r") as file:
            dataFromJson = json.load(file)
            dataframe = pd.json_normalize(data, record_path=["data"])
            csv_filename = f"leipzig_data_{i + 1}.csv"
            dataframe.to_csv(csv_filename, index=False)
            print(f"Daten erfolgreich als {csv_filename} gespeichert.")
    else:
        print(f"Fehler beim Abrufen der Daten (Statuscode: {response.status_code}).")

    if i < anzahl_anfragen - 1:
        print(f"Warte {zeitversatz} Sekunden bis zur nächsten Anfrage...")
        time.sleep(zeitversatz)
"""
# JSON-Daten in Tabellenformat transformieren
dataframes = []
for i in range(anzahl_anfragen):
    filename = f"leipzig_data_{i + 1}.json"
    with open(filename, "r") as file:
        data = json.load(file)
        dataframe = pd.json_normalize(data)
        dataframes.append(dataframe)

# Daten in CSV-Datei speichern
combined_dataframe = pd.concat(dataframes, ignore_index=True)
csv_filename = "leipzig_data_combined.csv"
combined_dataframe.to_csv(csv_filename, index=False)
print(f"Daten erfolgreich als {csv_filename} gespeichert.")
"""
