import requests
import pandas as pd
import json

import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

def send_rest_request():
    print("Sende Anfrage...")
    response = requests.get("https://platform.tier-services.io/v2/vehicle?zoneId=LEIPZIG",
                            headers={"X-API-Key": "bpEUTJEBTf74oGRWxaIcW7aeZMzDDODe1yBoSxi2"})
    return response

def plot_battery_histogram(dataframe):
    plt.figure(figsize=(10, 6))
    plt.hist(dataframe['attributes.batteryLevel'], bins=20, alpha=0.7)
    plt.xlabel('Batterieladestand (%)')
    plt.ylabel('Anzahl der E-Scooter')
    plt.title('Verteilung des Batterieladestands der E-Scooter')
    plt.show()

def plot_range_boxplot(dataframe):
    plt.figure(figsize=(10, 6))
    plt.boxplot(dataframe['attributes.currentRangeMeters'])
    plt.ylabel('Reichweite (Meter)')
    plt.title('Verteilung der Reichweite der E-Scooter')
    plt.show()

def plot_speed_histogram(dataframe):
    plt.figure(figsize=(10, 6))
    plt.hist(dataframe['attributes.maxSpeed'], bins=15, alpha=0.7)
    plt.xlabel('Maximale Geschwindigkeit (km/h)')
    plt.ylabel('Anzahl der E-Scooter')
    plt.title('Verteilung der maximalen Geschwindigkeit der E-Scooter')
    plt.show()

def plot_zone_bar_chart(dataframe):
    zone_counts = dataframe['attributes.zoneId'].value_counts()
    plt.figure(figsize=(10, 6))
    zone_counts.plot(kind='bar')
    plt.xlabel('Zone')
    plt.ylabel('Anzahl der E-Scooter')
    plt.title('Anzahl der aktiven E-Scooter pro Zone')
    plt.xticks(rotation=45)
    plt.show()


def plot_choropleth_map(dataframe, geojson_data, location_column, color_column, title):
    fig = px.choropleth_mapbox(dataframe, geojson=geojson_data, locations=location_column, color=color_column,
                               featureidkey="properties.zoneId", color_continuous_scale="Viridis",
                               mapbox_style="carto-positron", zoom=10, center={"lat": dataframe['attributes.lat'].mean(),
                               "lon": dataframe['attributes.lng'].mean()}, title=title)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

def plot_3d_scatterplot(dataframe, title):
    fig = px.scatter_3d(dataframe, x='attributes.lng', y='attributes.lat', z='attributes.batteryLevel',
                        color='attributes.batteryLevel', opacity=0.7, title=title)
    fig.show()

def plot_pie_chart(dataframe, labels_column, values_column, title):
    fig = px.pie(dataframe, values=values_column, names=labels_column, title=title)
    fig.show()

def plot_heatmap(dataframe, title):
    fig = px.density_mapbox(dataframe, lat='attributes.lat', lon='attributes.lng', z='attributes.batteryLevel',
                             radius=10, center=dict(lat=dataframe['attributes.lat'].mean(),
                             lon=dataframe['attributes.lng'].mean()), zoom=10, mapbox_style="carto-positron",
                             title=title)
    fig.show()

def plot_animated_map(dataframe, title):
    fig = px.scatter_mapbox(dataframe, lat='attributes.lat', lon='attributes.lng', animation_frame='attributes.lastLocationUpdate',
                            color='attributes.batteryLevel', size_max=15, zoom=10, mapbox_style="carto-positron",
                            title=title)
    fig.show()


def plot_map_with_marker_colors(dataframe):
    fig = go.Figure(go.Scattermapbox(
            lat=dataframe['attributes.lat'],
            lon=dataframe['attributes.lng'],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=10,
                color=dataframe['attributes.batteryLevel'],
                colorscale='Viridis',
                colorbar=dict(title='Batterieladestand')
            ),
            text=dataframe['attributes.licencePlate']
    ))

    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=10,
        mapbox_center = {"lat": dataframe['attributes.lat'].mean(), "lon": dataframe['attributes.lng'].mean()}
    )

    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

def plot_geographical_distribution(dataframe):
    plt.figure(figsize=(10, 6))
    plt.scatter(dataframe['attributes.lng'], dataframe['attributes.lat'], s=dataframe['attributes.batteryLevel']*10, alpha=0.5)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Geographische Verteilung der E-Scooter-Standorte')
    plt.show()

# Funktion zum Abrufen von Daten und Ausführen der Visualisierungen
def visualize_scooter_data():
    response = send_rest_request()

    if response.status_code == 200:
        data = response.json()
        filename = f"leipzig_data_sa.json"
        with open(filename, "w") as file:
            json.dump(data, file)
        print(f"Daten erfolgreich in {filename} gespeichert.")
        with open(filename, "r") as file:
            dataFromJson = json.load(file)
            dataframe = pd.json_normalize(data, record_path=["data"])
            csv_filename = f"leipzig_data_sa.csv"
            dataframe.to_csv(csv_filename, index=False)
            print(f"Daten erfolgreich als {csv_filename} gespeichert.")

            # Aufruf der Visualisierungsfunktionen
            plot_battery_histogram(dataframe)
            #plot_range_boxplot(dataframe)
            #plot_speed_histogram(dataframe)
            #plot_zone_bar_chart(dataframe)
            plot_map_with_marker_colors(dataframe)
            #plot_geographical_distribution(dataframe)
            #geht nicht plot_choropleth_map(dataframe, geojson_data, location_column='attributes.zoneId', color_column='Anzahl_der_E-Scooter', title='E-Scooter-Verteilung nach Bezirken')
            #plot_3d_scatterplot(dataframe, title='3D-Scatterplot der E-Scooter-Standorte')
            #geht nicht plot_pie_chart(dataframe, labels_column='vehicleType', values_column='Anzahl', title='Verteilung der Fahrzeugtypen')
            plot_heatmap(dataframe, title='Heatmap der Batterieladestände in verschiedenen Zonen')
            #plot_animated_map(dataframe, title='Animierte Karte der E-Scooter-Bewegungen im Zeitverlauf')

    else:
        print(f"Fehler beim Abrufen der Daten (Statuscode: {response.status_code}).")

# Aufruf der Funktion zum Ausführen der Visualisierungen
visualize_scooter_data()

