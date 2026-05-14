🚀 Dashboard ENEM 2024: Panorama Educacional Brasileiro
Status do Projeto: Em desenvolvimento (Fase de Visualização) 📈

Este projeto documenta o ciclo completo de um dado: da extração bruta à inteligência de negócio.

🎯 Objetivo
Transformar os microdados do ENEM 2024 (mais de 4,3 milhões de registros) em insights visuais acionáveis, superando desafios críticos de infraestrutura e performance que simulam um ambiente real de engenharia de dados.

🛠️ Stack Tecnológica
Linguagem: Python 3.x (Pandas, PyArrow)

Banco de Dados: PostgreSQL rodando via Docker

BI: Power BI (DAX Avançado)

Versionamento: Git (Otimizado para grandes volumes)


🏗️ Arquitetura e Desafios Superados
1. Ambiente Isolado com Docker
Para garantir que o projeto seja replicável e não dependa de instalações locais complexas:

O que fiz: Configurei um ambiente de banco de dados PostgreSQL totalmente containerizado.

Ponto Forte: Uso de docker-compose para orquestração, permitindo subir todo o backend do projeto com um único comando.

2. Engenharia de Dados e Otimização (O "Iceberg")
Este foi o ponto de maior aprendizado técnico. Lidar com arquivos de 1.6 GB exigiu estratégias de compressão:

Desafio: O limite de 100MB do GitHub e a lentidão do CSV.

Solução: Implementação de conversão para Parquet com compressão Snappy.

Resultado Extraordinário: * Redução do volume de dados em 84%.

O arquivo de 444MB passou para apenas 71MB, mantendo 100% da integridade.

3. Modelagem SQL e Business Intelligence
A inteligência por trás dos gráficos:

ETL: Scripts Python personalizados para carga de dados em massa.

DAX: Desenvolvimento de medidas complexas, como a Média por Área, garantindo que o dashboard reflita métricas pedagógicas reais e não apenas cálculos estatísticos básicos.

🧠 Lições Aprendidas (Highlights)
✅ Gestão de Crise em Git: Limpeza de histórico e uso de .gitignore para dados sensíveis/pesados.

✅ Performance: Por que o formato colunar (Parquet) é o padrão da indústria para Big Data.

✅ UX para Dados: A importância de um layout limpo e focado no usuário final.

📸 Preview do Dashboard





