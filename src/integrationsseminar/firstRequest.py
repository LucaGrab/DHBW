import requests
import time
import json
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.orc as orc
from fastavro import writer, parse_schema

def pandas_type_to_avro_type(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return "int"
    elif pd.api.types.is_float_dtype(dtype):
        return "float"
    elif pd.api.types.is_string_dtype(dtype):
        return "string"
    elif pd.api.types.is_bool_dtype(dtype):
        return "boolean"
    # Fügen Sie hier weitere Datentypkonvertierungen nach Bedarf hinzu
    else:
        return "string"  # Standardfall oder Fehlerbehandlung

# Erstellen Sie das Schema dynamisch basierend auf den Datentypen der DataFrame-Spalten
def create_dynamic_avro_schema(dataframe, record_name="Data"):
    fields = []
    for column in dataframe.columns:
        dtype = dataframe[column].dtype
        avro_type = pandas_type_to_avro_type(dtype)
        fields.append({"name": column, "type": ["null", avro_type], "default": None})
    
    schema = {
        "type": "record",
        "name": record_name,
        "fields": fields
    }
    return schema

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
        parquet_filename = f"leipzig_data_{i + 1}.parquet"
        table = pa.Table.from_pandas(dataframe)
        pq.write_table(table, parquet_filename)
        print(f"Daten erfolgreich als {parquet_filename} gespeichert.")
        orc_filename = f"leipzig_data_{i + 1}.orc"
        orc.write_table(table, orc_filename)
        print(f"Daten erfolgreich als {orc_filename} gespeichert.")
        # Anwendung der Funktion und Speichern im Avro-Format
        avro_filename = f"leipzig_data_{i + 1}.avro"
        dynamic_schema = create_dynamic_avro_schema(dataframe)
        parsed_schema = parse_schema(dynamic_schema)

        with open(avro_filename, "wb") as file:
            writer(file, parsed_schema, dataframe.to_dict("records"))
        print(f"Daten erfolgreich als {avro_filename} gespeichert.")

        """avro_filename = f"leipzig_data_{i + 1}.avro"
        schema = {
            "type": "record",
            "name": "Data",
            "fields": [
                {"name": column, "type": ["null", "string"]} if column not in ["attributes.batteryLevel", "attributes.currentRangeMeters", "attributes.lat"]
                else {"name": column, "type": ["null", "int"]} if column in ["attributes.batteryLevel", "attributes.currentRangeMeters"]
                else {"name": column, "type": ["null", "float"]} for column in dataframe.columns
            ]      
        }
        parsed_schema = parse_schema(schema)
        with open(avro_filename, "wb") as file:
            writer(file, parsed_schema, dataframe.to_dict("records"))
        print(f"Daten erfolgreich als {avro_filename} gespeichert.")
        """
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
