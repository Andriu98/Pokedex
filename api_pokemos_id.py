import requests
url  = 'https://pokeapi.co/api/v2/pokemon?limit=1000'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    pokemon_list = data['results']
    
    for pokemon in pokemon_list:
        name = pokemon['name']
        # El ID del Pokémon está al final de la URL
        id = pokemon['url'].split('/')[-2]
        print(f"{name.capitalize()} - ID: {id}")
else:
    print(f"Error al obtener los Pokémon (código de estado {response.status_code})")

