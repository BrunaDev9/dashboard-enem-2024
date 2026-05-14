# 📋 Dashboard ENEM 2024: Panorama Educacional Brasileiro

> **Status do Projeto:** Em desenvolvimento (Fase de Visualização) 🔲

Este projeto documenta o ciclo completo de um dado: da extração bruta à inteligência de negócio.

---

## 🎯 Objetivo

Transformar os microdados do **ENEM 2024** (mais de **4,3 milhões de registros**) em insights visuais acionáveis, superando desafios críticos de infraestrutura e performance que simulam um ambiente real de engenharia de dados.

---

## 🛠️ Stack Tecnológica

- **Linguagem:** Python 3.x (Pandas, PyArrow)
- **Banco de Dados:** PostgreSQL rodando via Docker
- **BI:** Power BI (DAX Avançado)
- **Versionamento:** Git (Otimizado para grandes volumes)

---

## 🏗️ Arquitetura e Desafios Superados

### 1. Ambiente Isolado com Docker
Para garantir que o projeto seja replicável e não dependa de instalações locais complexas:

- **O que fiz:** Configurei um ambiente de banco de dados PostgreSQL totalmente containerizado.
- **Ponto Forte:** Uso de `docker-compose` para orquestração, permitindo subir todo o backend do projeto com um único comando.

### 2. Engenharia de Dados e Otimização (O "Iceberg")
Este foi o ponto de maior aprendizado técnico. Lidar com arquivos de **1.6 GB** exigiu estratégias de compressão:

- **Conversão para Parquet:** Redução drástica no tamanho dos arquivos e ganho de performance nas queries.
- **Tipagem Explícita:** Definição manual dos dtypes do Pandas para evitar consumo excessivo de memória.
- **Ingestão em Chunks:** Carregamento dos dados em lotes para não sobrecarregar a RAM durante a importação.

### 3. Pipeline de Dados Completo
Construção de um pipeline de ponta a ponta:

- **Extração:** Download e leitura dos microdados oficiais do INEP.
- **Transformação:** Limpeza, padronização e modelagem dimensional (`script_modelagem.sql`).
- **Carga:** Ingestão otimizada no PostgreSQL via `import_data.py`.

---

## 🚀 Destaques Técnicos

- **Processamento de Dados:** Manipulação de dataset real com mais de 4,3 milhões de registros brutos.
- **Data Wrangling:** Limpeza de dados complexos, tratamento de tipos (Casting) e higienização de nulos.
- **Modelagem Dimensional:** Estruturação dos dados em esquema otimizado para consultas analíticas.
- **Visualização Avançada:** Criação de relatórios interativos no Power BI com medidas DAX customizadas.
- **Infraestrutura como Código:** Ambiente 100% reproduzível via `docker-compose`.

---

## 🗂️ Estrutura do Projeto

```
dashboard-enem-2024/
│
├── 📄 .gitignore
├── 📊 PARTICIPANTES_2024.parquet    # Dataset comprimido
├── 🐍 convert_to_parquet.py         # Conversão CSV → Parquet
├── 🐳 docker-compose.yml            # Orquestração do ambiente
├── 🐍 import_data.py                # Ingestão no PostgreSQL
├── 📓 limpeza_enem.ipynb            # Notebook de limpeza e EDA
└── 🗃️ script_modelagem.sql          # Modelagem dimensional
```

---

## ▶️ Como Executar

**1. Clone o repositório**
```bash
git clone https://github.com/BrunaDev9/dashboard-enem-2024.git
cd dashboard-enem-2024
```

**2. Suba o ambiente com Docker**
```bash
docker-compose up -d
```

**3. Converta os dados para Parquet**
```bash
python convert_to_parquet.py
```

**4. Importe os dados no PostgreSQL**
```bash
python import_data.py
```

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Bibliotecas:** Pandas, PyArrow, SQLAlchemy
- **Banco de Dados:** PostgreSQL 15
- **Containerização:** Docker, Docker Compose
- **BI & Visualização:** Power BI (DAX)
- **Versionamento:** Git + GitHub (com `.gitignore` otimizado para arquivos grandes)

---

## 👩‍💻 Autora

**BrunaDev9 — Bruna Veras**

[![GitHub](https://img.shields.io/badge/GitHub-BrunaDev9-181717?style=flat&logo=github)](https://github.com/BrunaDev9)
