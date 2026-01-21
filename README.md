# MTG Market Watcher 🧙‍♂️

Plataforma para monitoramento e análise de preços de cartas de *Magic: The Gathering*.

## 🏗 Arquitetura

| Diretório    | Responsabilidade      | Tecnologias                      |
| :---         | :---                  | :---                             |
| `/miner`     | Coleta de Dados       | Python, Scryfall API             |
| `/backend`   | API & Persistência    | Java 21, Spring Boot, PostgreSQL |
| `/frontend`  | Dashboard             | Angular 19, Angular Material     |
| `/docker`    | Infraestrutura        | Docker Compose                   |

## ✅ Implementado

### Backend (Spring Boot)
- ✅ Entidade `Carta` e Repository JPA.
- ✅ Service layer com lógica de negócio.
- ✅ Ingestão de dados via `/api/ingestao/cartas` (POST).
- ✅ Consulta de dados via `/api/cartas` (GET).
- ✅ Configuração PostgreSQL via Docker.

### Frontend (Angular)
- ✅ Estrutura inicial do projeto Angular.
- ✅ Integração com API Backend (Service de Cartas).
- ✅ Componentes de UI: Lista de Cartas, Histórico de Preços (Dialog), Mensagens de Erro.
- ✅ Angular Material para UI/UX.

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
O backend estará disponível em `http://localhost:8080`.

### 3. Rodar o Frontend
```bash
cd frontend
npm install
npm start
```
O frontend estará disponível em `http://localhost:4200`.

### 4. Minerador (Python)
```bash
cd miner
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python scryfall_miner.py
```

## 📡 Endpoints Disponíveis

| Método | Endpoint                | Descrição                           |
|--------|-------------------------|-------------------------------------|
| POST   | `/api/ingestao/cartas`  | Recebe dados de cartas do minerador |
| GET    | `/api/cartas`           | Retorna a lista de cartas           |
| GET    | `/api/cartas/{id}`      | Retorna detalhes de uma carta       |

## 🔧 Próximos Passos

- [ ] Melhorar visualização com gráficos de preço.
- [ ] Implementar filtros de busca e ordenação.
- [ ] Sistema de alertas de preço.
- [ ] Autenticação e Favoritos.

---

**Status:** 🚧 MVP em desenvolvimento (Frontend Integrado)