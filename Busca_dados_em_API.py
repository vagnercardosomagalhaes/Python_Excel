import requests
import pandas as pd
import hashlib

public_key = '03409009f96d9a9c54e94ea1b72c0553'
private_key = '89f8aec4fbbb1b01446ddf8240fbc9242c4ed39b'
ts = '1'

# === GERA HASH MD5 ===
to_hash = ts + private_key + public_key
hash_val = hashlib.md5(to_hash.encode()).hexdigest()

# === FAZ REQUISIÇÃO ===
url = f'https://gateway.marvel.com/v1/public/characters?ts={ts}&apikey={public_key}&hash={hash_val}'
response = requests.get(url)

# Verifica se a resposta foi bem sucedida
if response.status_code != 200:
    print(f"Erro na requisição: {response.status_code}")
    print(response.text)
    exit()

# Converte resposta em JSON
data = response.json()

# Valida estrutura do JSON
if 'data' in data and 'results' in data['data']:
    characters = data['data']['results']
    
    # Verifica se characters é mesmo uma lista
    if isinstance(characters, list):
        character_list = []
        for char in characters:
            character_list.append({
                'Nome': char.get('name', ''),
                'Descrição': char.get('description', '')
            })

        # Cria e exporta o DataFrame
        df = pd.DataFrame(character_list)
        df.to_excel('Personagens_Marvel.xlsx', index=False)
        print("Exportação finalizada com sucesso!")
        print(df.head())
    else:
        print("Erro: 'results' não é uma lista.")
        print(type(characters), characters)
else:
    print("Erro: estrutura inesperada da resposta.")
    print(data)