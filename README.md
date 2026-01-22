# MTG Market Watcher 🧙‍♂️

Sistema completo para monitoramento de preços de cartas de Magic: The Gathering com coleta automática de dados e interface web.

## 🏗 Arquitetura

| Componente   | Tecnologia                        | Porta |
|--------------|-----------------------------------|-------|
| Frontend     | Angular 19 + Material Design     | 4200  |
| Backend      | Spring Boot + PostgreSQL         | 8080  |
| Database     | PostgreSQL 15                     | 5433  |
| Miner        | Python + Scryfall + LigaMagic    | -     |

## ✅ Funcionalidades

- **Coleta Automática**: Preços em USD, EUR, TIX (Scryfall) e BRL (LigaMagic)
- **Interface Web**: Dashboard responsivo com Angular Material
- **Histórico Completo**: Armazenamento e visualização do histórico de preços
- **API REST**: Endpoints para integração e consulta de dados
- **Execução Agendada**: Coleta automática a cada 30 minutos

## 🚀 Execução

### 1. Banco de Dados
```bash
cd docker
docker-compose up -d
```

### 2. Backend
```bash
cd backend
./mvnw spring-boot:run
```

### 3. Frontend
```bash
cd frontend
npm install
npm start
```

### 4. Minerador (Primeira execução)
```bash
cd miner
pip install -r requirements.txt
python run_miner.py
```

### Scripts Windows
- **Execução única**: `start_miner.bat`
- **Execução agendada**: `start_miner_scheduled.bat`

## 📊 Cartas Monitoradas

- Lightning Bolt
- Sol Ring  
- Black Lotus
- Ragavan, Nimble Pilferer
- Sheoldred, the Apocalypse
- Teferi, Time Raveler
- Oko, Thief of Crowns
- Jace, the Mind Sculptor
- Tarmogoyf
- Snapcaster Mage

## 🔧 API Endpoints

| Método | Endpoint               | Descrição                    |
|--------|------------------------|------------------------------|
| GET    | `/api/cartas`          | Lista todas as cartas        |
| GET    | `/api/cartas/{id}`     | Detalhes de uma carta        |
| POST   | `/api/ingestao/cartas` | Ingestão de dados (interno)  |

## ⚠️ Troubleshooting

**Frontend não mostra dados:**
1. Verifique se o backend está rodando: `http://localhost:8080/api/cartas`
2. Execute o minerador: `python run_miner.py`
3. Confirme se o banco está ativo: `docker ps`

**Erro de conexão com banco:**
```bash
cd docker
docker-compose down
docker-compose up -d
```

---

**Status:** ✅ MVP Funcional