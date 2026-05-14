import pandas as pd
from sqlalchemy import create_engine
import sys

# Configurações do banco de dados (mesmas do docker-compose)
DB_USER = 'postgres'
DB_PASSWORD = 'mysecretpassword'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'enem_db'

# Arquivo CSV de origem
CSV_FILE = 'RESULTADOS_2024.csv'
# Nome da tabela no banco de dados
TABLE_NAME = 'resultados_2024'

def main():
    print(f"Lendo o arquivo {CSV_FILE}...")
    try:
        # Lendo o arquivo CSV com parâmetros para arquivos do Brasil (IBGE, INEP, etc)
        # sep=';' para separador e encoding='latin-1' para acentos
        df = pd.read_csv(CSV_FILE, sep=';', encoding='latin-1') 
        print(f"Arquivo lido com sucesso! {len(df)} linhas encontradas.")
        
        print("Iniciando o tratamento dos dados...")
        # 1. Remover notas nulas em MT e Redação
        df = df.dropna(subset=['NU_NOTA_MT', 'NU_NOTA_REDACAO'])
        
        # 2. Filtrar alunos presentes em Matemática e Linguagens
        df = df[(df['TP_PRESENCA_MT'] == 1) & (df['TP_PRESENCA_LC'] == 1)]
        
        # 3. Calcular a média geral
        notas_colunas = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
        colunas_disponiveis = [col for col in notas_colunas if col in df.columns]
        df['MEDIA_GERAL'] = df[colunas_disponiveis].mean(axis=1)
        
        # 4. Selecionar apenas as colunas desejadas
        colunas_finais = [
    'SG_UF_PROVA', 'NO_MUNICIPIO_PROVA', 'NU_NOTA_CN', 'NU_NOTA_CH', 
    'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO', 'MEDIA_GERAL', 
    'TP_DEPENDENCIA_ADM_ESC'
]
        # Garante que só tentará selecionar as colunas se elas existirem no arquivo
        colunas_selecionadas = [col for col in colunas_finais if col in df.columns]
        df = df[colunas_selecionadas]
        
        print(f"Tratamento concluído! {len(df)} linhas prontas para importação.")
        
    except FileNotFoundError:
        print(f"Erro: O arquivo '{CSV_FILE}' não foi encontrado no diretório atual.")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
        sys.exit(1)

    print("Conectando ao banco de dados PostgreSQL...")
    # Criando a string de conexão SQLAlchemy
    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

    try:
        print(f"Inserindo os dados na tabela '{TABLE_NAME}'...")
        # if_exists='replace' recria a tabela.
        # chunksize ajuda na performance ao enviar dados em lotes (bom para arquivos grandes do ENEM)
        df.to_sql(TABLE_NAME, engine, if_exists='replace', index=False, chunksize=10000)
        print("🎉 Dados importados para o banco com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar os dados no banco: {e}")

if __name__ == "__main__":
    main()
