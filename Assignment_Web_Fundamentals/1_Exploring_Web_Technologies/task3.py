import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def calculate_average_weight(pokemon_list):
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data_list = [fetch_pokemon_data(name) for name in pokemon_names]

for data in pokemon_data_list:
    if data:
        name = data['name']
        abilities = [ability['ability']['name'] for ability in data['abilities']]
        print(f"Name: {name}")
        print(f"Abilities: {', '.join(abilities)}")
    else:
        print("Failed to fetch data.")

average_weight = calculate_average_weight(pokemon_data_list)
print(f"Average Weight: {average_weight}")
