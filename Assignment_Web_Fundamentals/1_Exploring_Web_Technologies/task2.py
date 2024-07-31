import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

pokemon_name = "pikachu"
data = fetch_pokemon_data(pokemon_name)

if data:
    name = data['name']
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    print(f"Name: {name}")
    print(f"Abilities: {', '.join(abilities)}")
else:
    print("Failed to fetch data.")
