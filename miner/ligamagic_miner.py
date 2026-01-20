import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re

def get_preco_ligamagic(nome_carta):
    url = f"https://www.ligamagic.com.br/?view=cards/card&card={nome_carta}"

    #User-Agente para evitar bloqueios (403)
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    try: 
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            print(f"[LigaMagic] Erro HTTP: {response.status_code}")
            return None
            
        soup = BeautifulSoup(response.text, 'html.parser')

        box_precos = soup.find('div', id='precos-fisc')
        preco_encontrado = None
        
        if box_precos:
            texto = box_precos.get_text()
        else:
            texto = soup.get_text()
            
        match = re.search(r'Mínimo:.*?R\$\s*([\d\.,]+)', texto, re.IGNORECASE)

        if match:
            valor_str = match.group(1)
            # Conversão Brasil -> Python (Tira ponto de milhar, troca virgula por ponto)
            # Ex: "1.200,50" -> "1200.50"
            valor_clean = valor_str.replace('.', '').replace(',', '.')
            preco_encontrado = float(valor_clean)
            print(f"   [LigaMagic] 💰 Preço encontrado: R$ {preco_encontrado}")
            return preco_encontrado
            
        print(f"   [LigaMagic] ⚠️ Preço não localizado no HTML para: {nome_carta}")
        return None

    except Exception as e:
        print(f"   [LigaMagic] 🚨 Erro de conexão/parse: {e}")
        return None

# Bloco para testar apenas este arquivo isoladamente
if __name__ == "__main__":
    print("--- Teste Unitário LigaMagic ---")
    teste = "Sheoldred, the Apocalypse"
    preco = get_preco_ligamagic(teste)
    print(f"Resultado final: {preco}")