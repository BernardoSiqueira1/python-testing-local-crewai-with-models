# CrewAI Local News Agent

Teste de inteligência artificial para coleta de notícias usando:

- CrewAI
- Ollama
- SQLite

- BeautifulSoup
- Feedparser
- Requests

Pipeline multi-agentes para:

- coleta
- curadoria
- classificação
- detecção de hot news
- resumos executivos
- relatório semanal

Testado em uma máquina com as seguintes specs:

- Intel(R) Core(TM) i5-10400F CPU (12 cores, 2.90 GHz)
- 16GB RAM DDR4, 3200 MHz  
- NVIDIA GeForce RTX 3060 - 8GB VRAM GDDR6

---

# Arquitetura

```txt
RSS / API / scraping
        ↓
Collector Agent
        ↓
SQLite
        ↓
Classifier Agent
        ↓
Hot News Detector
        ↓
Summarizer Agent
        ↓
Weekly Editor
        ↓
Markdown Report
```

---

# Estrutura do Projeto

```txt
crewai-local-news-agent/
│
├── agents/
│   ├── agents.py
│   ├── tasks/
│   └── services/
│
├── collectors/
│   ├── hackernews.py
│   ├── github_trending.py
│   ├── rss_parser.py
│   └── unified_collector.py
│
├── persistence/
│   ├── news_db.py
│   └── repository.py
│
├── reports/
│
├── news_collector.py
├── requirements.txt
└── README.md
```

---

# Requisitos

- Python 3.11+
- Ollama instalado
- Modelo qwen2.5-coder:7b baixado

---

# Instalação e uso

## 1. Clone o projeto

```bash
git clone <repo>
cd crewai-local-news-agent
```

---

## 2. Crie um ambiente virtual

```bash
python -m venv .env
```

---

## 3. Ative o ambiente virtual

### Linux/macOS

```bash
source .env/bin/activate
```

### Windows

```bash
.env\Scripts\activate
```

---

## 4. Instale as dependências do projeto

```bash
pip install -r requirements.txt
```

---

# Instalação do Ollama

## Linux/macOS

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

# Baixe o modelo

```bash
ollama pull qwen2.5-coder:7b
```

---

# Inicie o Ollama

```bash
ollama serve
```

---

# Testando Ollama

```bash
ollama run qwen2.5-coder:7b
```

Se responder, então está funcionando.

---

# Rodando o Projeto

## Execute o pipeline

```bash
python news_collector.py
```

---

# O que acontece ao rodar

O sistema:

1. Coleta notícias:
   - Wired RSS
   - Hacker News
   - GitHub Trending

2. Curadoria via Collector Agent

3. Salva notícias no SQLite

4. Classifica:
   - categoria
   - relevância
   - impacto

5. Detecta Hot News

6. Gera resumos das noticias

7. Cria relatório semanal em Markdown

Obs: Itens como: banco de dados, arquivos, etc. Serão gerados automaticamente ao rodar news_collector.py

---

# Banco SQLite

Arquivo:

```txt
news_database.db
```

Tabela principal:

```sql
news
```

---

# Relatórios

Os relatórios semanais são salvos em:

```
reports/
```

---
