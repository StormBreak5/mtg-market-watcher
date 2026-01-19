# MTG Market Watcher 🧙‍♂️

Plataforma para monitoramento e análise de preços de cartas de *Magic: The Gathering*.

## 🏗 Arquitetura

| Diretório    | Responsabilidade      | Tecnologias          |
| :---         | :---                  | :---                 |
| `/miner`     | Coleta de Dados       | Python, Scryfall API |
| `/backend`   | API & Persistência    | Java 21, Spring Boot, PostgreSQL |
| `/frontend`  | Dashboard             | Angular (planejado)  |
| `/docker`    | Infraestrutura        | Docker Compose       |

## ✅ Implementado

### Backend (Spring Boot)
- ✅ Entidade `Carta` com campos: nome, edição, preço, raridade, tipo, etc.
- ✅ Repository JPA para persistência
- ✅ Service layer com lógica de negócio
- ✅ Endpoint REST `/api/ingestao/cartas` (POST) para receber dados do minerador
- ✅ Configuração PostgreSQL via Docker

### Banco de Dados
- ✅ PostgreSQL 15 rodando via Docker Compose
- ✅ Schema criado automaticamente pelo Hibernate

## 🚀 Como Rodar

### 1. Subir o Banco de Dados
```bash
cd docker
docker-compose up -d
```

### 2. Rodar o Backend
```bash
cd backend
./mvnw spring-boot:run
```

O backend estará disponível em `http://localhost:8080`

### 3. Minerador (Python)
```bash
cd miner
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python scryfall_miner.py
```

## 📡 Endpoints Disponíveis

| Método | Endpoint                | Descrição                    |
|--------|-------------------------|------------------------------|
| POST   | `/api/ingestao/cartas`  | Recebe dados de cartas do minerador |

## 🔧 Próximos Passos

- [ ] Endpoints de consulta (GET)
- [ ] Frontend Angular
- [ ] Integração completa miner → backend
- [ ] Dashboard de visualização de preços

---

**Status:** 🚧 MVP em desenvolvimento