import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['bodies']
    else:
        return []

def display_planet_data(planets):
    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName', 'N/A')
            mass = planet.get('mass', {}).get('massValue', 'N/A')
            orbit_period = planet.get('sideralOrbit', 'N/A')
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

planets = fetch_planet_data()
display_planet_data(planets)
