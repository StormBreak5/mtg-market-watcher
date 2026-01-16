import requests
import json
from datetime import datetime

SCRYFALL_API_URL = "https://api.scryfall.com/cards/named"

def buscar_carta(nome_carta):
    print(f"--- Buscando dados para: {nome_carta} ---")

    params = {'fuzzy': nome_carta}
    response = requests.get(SCRYFALL_API_URL, params=params)

    if response.status_code == 200:
        dados = response.json()
        
        carta_info = {
            "nome": dados.get("name"),
            "set": dados.get('set_name'),
            "raridade": dados.get('rarity'),
            "preco_usd": dados['prices'].get('usd'),
            "preco_eur": dados['prices'].get('eur'),
            "preco_tix": dados['prices'].get('tix'),
            "data_coleta": datetime.now().isoformat()
        }

        return carta_info
    else:
        print(f"Erro ao buscar {nome_carta}: {response.status_code}")
        return None

if __name__ == "__main__":
    cartas_alvo = ["Black Lotus", "Sol Ring", "Sheoldred, the Apocalypse"]
    
    resultado_coleta = []
    
    for carta in cartas_alvo:
        dados = buscar_carta(carta)
        if dados:
            resultado_coleta.append(dados)
            
    print("\n--- DADOS COLETADOS (Simulando envio para o Java) ---")
    print(json.dumps(resultado_coleta, indent=4))