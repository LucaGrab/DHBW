import requests
import pandas as pd
import json

import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
import numpy as np
from plotly import io
from mpl_toolkits.basemap import Basemap



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

from sklearn.cluster import KMeans
def cluster_points_kmeans(dataframe, num_clusters):
    # Datenpunkte für das K-Means-Clustering vorbereiten
    X = dataframe[['attributes.lat', 'attributes.lng']].values

    # K-Means-Modell anwenden
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(X)

    # Cluster-Zuweisungen erhalten
    labels = kmeans.labels_

    # Einzelne Cluster extrahieren
    clusters = {}
    for label in range(num_clusters):
        cluster_points = dataframe.iloc[labels == label]
        clusters[label] = cluster_points

    # Clusterzentren erhalten
    cluster_centers = kmeans.cluster_centers_

    return clusters, cluster_centers

def plot_cluster_centers(dataframe, clusters, cluster_centers):
    fig = go.Figure()

    for label in range(len(cluster_centers)):
        center = cluster_centers[label]
        cluster_size = len(clusters[label])
        fig.add_trace(go.Scattermapbox(
            lat=[center[0]],
            lon=[center[1]],
            mode='markers',
            marker=dict(
                size=cluster_size*2,
                color='blue',
                opacity=cluster_size/65,
                symbol='circle',
            ),
            text=f'Cluster {label}<br>Cluster Size: {cluster_size}',
            name=f'Cluster {label}'
        ))

    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=11,
        mapbox_center = {"lat": dataframe['attributes.lat'].mean(), "lon": dataframe['attributes.lng'].mean()},
        margin={"r":0,"t":0,"l":0,"b":0}
    )

    fig.show()




def cluster_and_plot(dataframe, num_clusters):
    # Datenpunkte für das K-Means-Clustering vorbereiten
    X = dataframe[['attributes.lat', 'attributes.lng']].values

    # K-Means-Modell anwenden
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(X)

    # Cluster-Zuweisungen erhalten
    labels = kmeans.labels_

    # Einzelne Cluster extrahieren
    dataframe['cluster'] = labels

    # Plotly-Figur erstellen
    fig = px.scatter_mapbox(dataframe, 
                            lat='attributes.lat', 
                            lon='attributes.lng', 
                            color='cluster',
                            color_continuous_scale=px.colors.qualitative.Vivid,
                            size_max=15,
                            zoom=10,
                            center={"lat": dataframe['attributes.lat'].mean(), 
                                    "lon": dataframe['attributes.lng'].mean()},
                            mapbox_style="carto-positron",
                            hover_name='attributes.licencePlate',
                            title="Clustered Points on Map"
                           )
    
    # Karte anzeigen
    fig.show()




def plot_cluster_centers_with_interactivity(dataframe, clusters, cluster_centers):
    fig = go.Figure()

    for label in range(len(cluster_centers)):
        center = cluster_centers[label]
        cluster_size = len(clusters[label])
        cluster_data = clusters[label]

        # Füge einen Kreis für das Clusterzentrum hinzu
        fig.add_trace(go.Scattermapbox(
            lat=[center[0]],
            lon=[center[1]],
            mode='markers',
            marker=dict(
                size=cluster_size * 5,
                color='blue',
                opacity=0.5,
                symbol='circle',
            ),
            text=f'Cluster {label}<br>Cluster Size: {cluster_size}',
            name=f'Cluster {label}',
            customdata=[label],  # Benutzerdefinierte Daten, um den Cluster zu identifizieren
            visible='legendonly'  # Setze den Kreis zunächst auf unsichtbar
        ))

        # Füge Datenpunkte für das Cluster hinzu
        fig.add_trace(go.Scattermapbox(
            lat=cluster_data['attributes.lat'],
            lon=cluster_data['attributes.lng'],
            mode='markers',
            marker=dict(
                size=5,
                color='red',
                opacity=0.5,
            ),
            text=cluster_data['attributes.licencePlate'],
            name=f'Cluster {label} Points',
            visible='legendonly'  # Setze den Kreis zunächst auf unsichtbar
        ))

    # Definiere die Interaktivität, um zwischen Clusterzentren und Datenpunkten umzuschalten
    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=10,
        mapbox_center={"lat": dataframe['attributes.lat'].mean(), "lon": dataframe['attributes.lng'].mean()},
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
    )

    fig.show()






def cluster2(dataframe, num_clusters):
    # Datenpunkte für das K-Means-Clustering vorbereiten
    X = dataframe[['attributes.lat', 'attributes.lng']].values

    # K-Means-Modell anwenden
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(X)

    # Cluster-Zuweisungen erhalten
    labels = kmeans.labels_

    # Einzelne Cluster extrahieren
    dataframe['cluster'] = labels

    return dataframe



def kMeansAnimation(dataframe, max_clusters):
    restructured_data = []
    
    for k in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(dataframe[['attributes.lat', 'attributes.lng']])
        labels = kmeans.labels_
        for i in range(len(dataframe)):
            restructured_data.append({'Zugehörigkeit': labels[i], 'AnzahlCluster': k})

    return pd.concat([dataframe] * max_clusters, ignore_index=True).assign(**pd.DataFrame(restructured_data))

def plot_animated_map(restructured_df, title):
    fig = px.scatter_mapbox(restructured_df, lat='attributes.lat', lon='attributes.lng', color='Zugehörigkeit', 
                     color_continuous_scale=px.colors.qualitative.Vivid, zoom=11, 
                     title=title, animation_frame='AnzahlCluster', mapbox_style="carto-positron",
                     range_color=[0, max(restructured_df['Zugehörigkeit'])], category_orders={'Zugehörigkeit': sorted(set(restructured_df['Zugehörigkeit']))})
    fig.show()

def allTimeDataPlotly():
    # Laden der Daten aus der CSV-Datei
    data = pd.read_csv("leipzig_data_sa_alltime.csv")

    # Annahme: Die Daten enthalten Spalten 'id' und 'currentRangeMeters' für die Scooter und die Strecke
    # Berechnung der Streckenveränderung für jeden Scooter
    data['distance_change'] = data.groupby('id')['attributes.currentRangeMeters'].diff()

    # Entfernen Sie NaN-Werte (erste Einträge für jeden Scooter haben keine vorherige Streckeninformation)
    data.dropna(subset=['distance_change'], inplace=True)

    # Wählen Sie die Top-Scooter basierend auf der Streckenveränderung aus
    top_scooter_ids = data.groupby('id')['distance_change'].sum().abs().nlargest(5).index

    # Daten für die ausgewählten Scooter auswählen
    top_scooter_data = data[data['id'].isin(top_scooter_ids)]


    # Ermitteln der fünf Scooter mit den meisten Einträgen
    #top_scooter_ids = data['id'].value_counts().index[:1]

    # Daten für die fünf Scooter auswählen
    #top_scooter_data = data[data['id'].isin(top_scooter_ids)]
    print(top_scooter_data['attributes.currentRangeMeters'])
    # Plot mit Plotly
    fig = px.scatter_mapbox(top_scooter_data, lat="attributes.lat", lon="attributes.lng", color="id", hover_name="attributes.currentRangeMeters",
                            zoom=13, mapbox_style="carto-positron")
    fig.show()

def allTimeData():
    # Laden der Daten aus der CSV-Datei
    data = pd.read_csv("leipzig_data_sa_alltime.csv")

    # Ermitteln der fünf Scooter mit den meisten Einträgen
    top_scooter_ids = data['id'].value_counts().index[:1]

    # Farben für die Scooter definieren
    colors = ['red', 'blue', 'green', 'orange', 'purple']

    # Initialisieren des Plots
    plt.figure(figsize=(10, 8))

    # Iteration über die fünf Scooter mit den meisten Einträgen
    for i, scooter_id in enumerate(top_scooter_ids):
        # Daten für den aktuellen Scooter auswählen
        scooter_data = data[data['id'] == scooter_id]
        print(scooter_data['attributes.lng'])
        # Plot der Streckenbewegung des Scooters
        plt.plot(scooter_data['attributes.lng'], scooter_data['attributes.lat'], marker='o', linestyle='-', color=colors[i], label=f'Scooter {i+1}')

    # Beschriftung und Legende hinzufügen
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Streckenbewegung der fünf Scooter mit den meisten Einträgen')
    plt.legend()

    # Anzeigen der Karte
    plt.grid(True)
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
            new_data_df = dataframe
            csv_filename = f"leipzig_data_sa.csv"
            dataframe.to_csv(csv_filename, index=False)
            print(f"Daten erfolgreich als {csv_filename} gespeichert.")

                    # Laden der vorhandenen Daten, wenn die Datei existiert
            try:
                existing_data_df = pd.read_csv("leipzig_data_sa_alltime.csv")
            except FileNotFoundError:
                existing_data_df = pd.DataFrame()

            # Filtern der neuen Daten, um nur diejenigen hinzuzufügen, die nicht bereits vorhanden sind
            if not existing_data_df.empty:
                existing_ids_last_update = existing_data_df[['id', 'attributes.lastLocationUpdate']]
                new_data_df = new_data_df.merge(existing_ids_last_update, on=['id', 'attributes.lastLocationUpdate'], how='left', indicator=True)
                new_data_df = new_data_df[new_data_df['_merge'] == 'left_only'].drop(columns=['_merge'])

            # Hinzufügen der neuen Daten zu den vorhandenen Daten
            combined_data_df = pd.concat([existing_data_df, new_data_df], ignore_index=True)

            # Speichern der kombinierten Daten in der CSV-Datei
            combined_data_df.to_csv("leipzig_data_sa_alltime.csv", index=False)
            print("Daten erfolgreich gespeichert.")


            allTimeDataPlotly()
            # Aufruf der Visualisierungsfunktionen
            #clusters_kmeans, cluster_centers_kmeans = cluster_points_kmeans(dataframe, 20)
            #plot_cluster_centers(dataframe, clusters_kmeans, cluster_centers_kmeans)
            #plot_cluster_centers_with_interactivity(dataframe, clusters_kmeans, cluster_centers_kmeans)
            #cluster_and_plot(dataframe,20)
            #restructured_df = kMeansAnimation(dataframe, 10)
            #plot_animated_map(restructured_df, title="Clustered Points on Map")
            #plot_battery_histogram(dataframe)
            #plot_range_boxplot(dataframe)
            #plot_speed_histogram(dataframe)
            #plot_zone_bar_chart(dataframe)
            #plot_map_with_marker_colors(dataframe)
            #plot_geographical_distribution(dataframe)
            #geht nicht plot_choropleth_map(dataframe, geojson_data, location_column='attributes.zoneId', color_column='Anzahl_der_E-Scooter', title='E-Scooter-Verteilung nach Bezirken')
            #plot_3d_scatterplot(dataframe, title='3D-Scatterplot der E-Scooter-Standorte')
            #geht nicht plot_pie_chart(dataframe, labels_column='vehicleType', values_column='Anzahl', title='Verteilung der Fahrzeugtypen')
            #plot_heatmap(dataframe, title='Heatmap der Batterieladestände in verschiedenen Zonen')
            #plot_animated_map(dataframe, title='Animierte Karte der E-Scooter-Bewegungen im Zeitverlauf')

    else:
        print(f"Fehler beim Abrufen der Daten (Statuscode: {response.status_code}).")

# Aufruf der Funktion zum Ausführen der Visualisierungen
visualize_scooter_data()

