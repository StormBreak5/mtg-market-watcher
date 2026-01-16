# MTG Market Watcher 🧙‍♂️

Plataforma escalável para monitoramento e análise de preços de cartas de *Magic: The Gathering* em tempo real.

## 🏗 Arquitetura do Projeto

O projeto segue o modelo de **Monorepo**, dividido em microsserviços e responsabilidades:

| Diretório    | Responsabilidade      | Tecnologias Principais          |
| :---         | :---                  | :---                            |
| `/miner`     | **Coleta de Dados** | Python, Requests, RabbitMQ      |
| `/backend`   | **API & Core** | Java 17, Spring Boot, PostgreSQL|
| `/frontend`  | **Dashboard** | Angular, TypeScript, Chart.js   |
| `/docker`    | **Infraestrutura** | Docker Compose                  |

## 🚀 Como Rodar (Dev Mode)

### Pré-requisitos
* Docker & Docker Compose
* Java 17+
* Python 3.10+
* Node.js 18+

### 1. Minerador (Python)
Responsável por buscar os preços atuais na API Scryfall.

```bash
cd miner
python -m venv venv
# Ativar venv
pip install -r requirements.txt
python scryfall_miner.py
```

### 2. Backend (Java)
*Em desenvolvimento...*

### 3. Frontend (Angular)
*Em desenvolvimento...*

---

**Status:** 🚧 Em construção (MVP)