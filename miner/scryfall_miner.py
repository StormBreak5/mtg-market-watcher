import requests
import json
from ligamagic_miner import get_preco_ligamagic 

API_BACKEND_URL = "http://localhost:8080/api/ingestao"
SCRYFALL_API_URL = "https://api.scryfall.com/cards/named"

def buscar_carta_completa(nome_carta):
    print(f"\n--- Processando: {nome_carta} ---")
    
    # 1. Busca metadados e Dólar (Scryfall)
    params = {'fuzzy': nome_carta}
    resp = requests.get(SCRYFALL_API_URL, params=params)
    
    if resp.status_code != 200:
        print("   ❌ Carta não encontrada no Scryfall")
        return None
        
    dados_scryfall = resp.json()
    
    # 2. Busca preço em Reais (LigaMagic)
    # A gente chama o módulo separado aqui!
    preco_brl = get_preco_ligamagic(dados_scryfall.get('name'))
    
    # 3. Monta o Objeto Final (Merge)
    payload = {
        "nome": dados_scryfall.get('name'),
        "setCode": dados_scryfall.get('set'),
        "raridade": dados_scryfall.get('rarity'),
        "precoUsd": dados_scryfall['prices'].get('usd'),
        "precoEur": dados_scryfall['prices'].get('eur'),
        "precoTix": dados_scryfall['prices'].get('tix'),
        "precoBrl": preco_brl # Aqui entra o dado da LigaMagic
    }
    
    return payload

def enviar_para_backend(payload):
    try:
        resp = requests.post(API_BACKEND_URL, json=payload)
        if resp.status_code == 200:
            print("   ✅ [Backend] Dados salvos com sucesso!")
        else:
            print(f"   ❌ [Backend] Erro: {resp.status_code}")
    except Exception as e:
        print(f"   🚨 [Backend] Backend offline? {e}")

if __name__ == "__main__":
    lista_cartas = ["Black Lotus", "Sol Ring", "Ragavan, Nimble Pilferer"]
    
    for carta in lista_cartas:
        dados = buscar_carta_completa(carta)
        if dados:
            enviar_para_backend(dados)