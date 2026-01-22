import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re
import json

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
            
        html_content = response.text
        
        # Método 1: Procurar por preços em formato JSON no JavaScript
        # Padrão: "preco":"49.90","precoFinal":"44.91"
        preco_pattern = r'"preco":"([\d\.,]+)"'
        precos_encontrados = re.findall(preco_pattern, html_content)
        
        if precos_encontrados:
            # Pega o primeiro preço encontrado e converte
            preco_str = precos_encontrados[0]
            preco_float = float(preco_str.replace(',', '.'))
            print(f"   [LigaMagic] 💰 Preço encontrado (JSON): R$ {preco_float}")
            return preco_float
        
        # Método 2: Procurar por precoFinal (preço com desconto)
        preco_final_pattern = r'"precoFinal":"([\d\.,]+)"'
        precos_finais = re.findall(preco_final_pattern, html_content)
        
        if precos_finais:
            # Pega o menor preço final encontrado
            precos_numericos = []
            for preco_str in precos_finais:
                try:
                    preco_float = float(preco_str.replace(',', '.'))
                    precos_numericos.append(preco_float)
                except:
                    continue
            
            if precos_numericos:
                menor_preco = min(precos_numericos)
                print(f"   [LigaMagic] 💰 Menor preço final encontrado: R$ {menor_preco}")
                return menor_preco
        
        # Método 3: Fallback - procurar no HTML tradicional
        soup = BeautifulSoup(html_content, 'html.parser')
        box_precos = soup.find('div', id='precos-fisc')
        
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
            print(f"   [LigaMagic] 💰 Preço encontrado (HTML): R$ {preco_encontrado}")
            return preco_encontrado
            
        print(f"   [LigaMagic] ⚠️ Preço não localizado para: {nome_carta}")
        return None

    except Exception as e:
        print(f"   [LigaMagic] 🚨 Erro de conexão/parse: {e}")
        return None

# Bloco para testar apenas este arquivo isoladamente
if __name__ == "__main__":
    print("--- Teste Unitário LigaMagic ---")
    teste = "Lightning Bolt"
    preco = get_preco_ligamagic(teste)
    print(f"Resultado final: {preco}")