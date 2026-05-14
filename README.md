🚀 Dashboard ENEM 2024: Panorama Educacional Brasileiro
Análise de mais de 4,3 milhões de registros utilizando uma arquitetura escalável e otimizada. Este projeto documenta a transição de dados brutos para uma estrutura de Business Intelligence profissional.

📈 Resumo da Jornada do Projeto
Este projeto não foi apenas sobre criar gráficos, mas sobre enfrentar os desafios reais de um Analista de Dados. Abaixo, pontuo as etapas e problemas superados ao longo desse projeto:

1. Infraestrutura e Armazenamento (Docker + PostgreSQL)
Antes de analisar, foi necessário garantir onde os dados morariam.

Desafio: Configurar um ambiente isolado e seguro para o banco de dados.

Solução: Implementação de um container Docker com PostgreSQL.

Destaque: Uso de docker-compose para subir o serviço de banco de dados, garantindo que o projeto seja replicável em qualquer máquina.

2. ETL e Limpeza de Dados (Python & SQL)
Os Microdados do ENEM são famosos por serem "sujos" e complexos.

Limpeza com Python: Tratamento de valores nulos e padronização de colunas utilizando Pandas.

Carga de Dados: Criação de scripts import_data.py para automatizar a inserção de milhões de linhas no PostgreSQL sem travar o sistema.

Modelagem: Escrita de scripts SQL (script_modelagem.sql) para organizar as tabelas de forma eficiente para o Power BI.

3. Otimização de Performance (A "Ponta do Iceberg")
O maior desafio técnico surgiu ao tentar versionar o projeto. Os arquivos CSV originais somavam mais de 1.6 GB.

Problema: Limites de upload do GitHub e lentidão no processamento.

Solução de Engenharia: Migração da arquitetura de armazenamento de CSV para Parquet com compressão Snappy.

Resultado: Redução de 84% no tamanho dos arquivos (ex: de 444MB para 71MB), permitindo o versionamento completo do projeto e uma leitura muito mais veloz no dashboard.

4. Storytelling e UX no Power BI
Com os dados limpos e otimizados, o foco mudou para a entrega de valor.

Cálculos DAX: Criação de métricas personalizadas, como a Média por Área (corrigindo lógicas iniciais de Min/Max) para refletir a realidade pedagógica.

Interface: Design focado no usuário, removendo elementos desnecessários (como logos não autorizados) para manter a sobriedade e o foco na informação.
🛠️ Tecnologias Utilizadas
Linguagem: Python (Pandas, PyArrow)

Banco de Dados: PostgreSQL & Docker

Visualização: Power BI (DAX & Power Query)

Versionamento: Git & GitHub
