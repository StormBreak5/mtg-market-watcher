#!/usr/bin/env python3
"""
Script para executar o minerador de dados do MTG Market Watcher
"""

import time
import schedule
from scryfall_miner import buscar_carta_completa, enviar_para_backend

# Lista de cartas para monitorar
CARTAS_PARA_MONITORAR = [
    "Lightning Bolt",
    "Sol Ring", 
    "Black Lotus",
    "Ragavan, Nimble Pilferer",
    "Sheoldred, the Apocalypse",
    "Teferi, Time Raveler",
    "Oko, Thief of Crowns",
    "Jace, the Mind Sculptor",
    "Tarmogoyf",
    "Snapcaster Mage"
]

def executar_mineracao():
    """Executa a mineração de dados para todas as cartas da lista"""
    print(f"\n{'='*50}")
    print(f"🚀 Iniciando mineração de dados - {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}")
    
    for carta in CARTAS_PARA_MONITORAR:
        try:
            dados = buscar_carta_completa(carta)
            if dados:
                enviar_para_backend(dados)
                time.sleep(2)  # Pausa entre requisições para não sobrecarregar as APIs
        except Exception as e:
            print(f"   ❌ Erro ao processar {carta}: {e}")
    
    print(f"\n✅ Mineração concluída - {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}\n")

def executar_uma_vez():
    """Executa a mineração uma única vez"""
    executar_mineracao()

def executar_agendado():
    """Executa a mineração em intervalos regulares"""
    print("🕐 Agendando mineração para executar a cada 30 minutos...")
    
    # Agenda a execução a cada 30 minutos
    schedule.every(30).minutes.do(executar_mineracao)
    
    # Executa uma vez imediatamente
    executar_mineracao()
    
    # Loop principal
    while True:
        schedule.run_pending()
        time.sleep(60)  # Verifica a cada minuto

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--schedule":
        executar_agendado()
    else:
        executar_uma_vez()