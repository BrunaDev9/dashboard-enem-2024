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
    print(f"Lendo {CSV_FILE}...")
    try:
        # Leitura com encoding Latin-1 e separador ';' (padrão INEP/ENEM)
        df = pd.read_csv(CSV_FILE, sep=';', encoding='latin-1') 
        print(f"{len(df)} registros carregados.")
        
        print("Iniciando tratamento dos dados...")
        # 1. Remover registros com notas nulas em MT e Redação
        df = df.dropna(subset=['NU_NOTA_MT', 'NU_NOTA_REDACAO'])
        
        # 2. Filtrar alunos presentes em Matemática e Linguagens
        df = df[(df['TP_PRESENCA_MT'] == 1) & (df['TP_PRESENCA_LC'] == 1)]
        
        # 3. Calcular média geral entre as cinco áreas de conhecimento
        notas_colunas = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
        colunas_disponiveis = [col for col in notas_colunas if col in df.columns]
        df['MEDIA_GERAL'] = df[colunas_disponiveis].mean(axis=1)
        
        # 4. Selecionar apenas as colunas necessárias para análise
        colunas_finais = [
            'SG_UF_PROVA', 'NO_MUNICIPIO_PROVA', 'NU_NOTA_CN', 'NU_NOTA_CH', 
            'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO', 'MEDIA_GERAL', 
            'TP_DEPENDENCIA_ADM_ESC'
        ]
        # Seleciona apenas as colunas disponíveis no arquivo
        colunas_selecionadas = [col for col in colunas_finais if col in df.columns]
        df = df[colunas_selecionadas]
        
        print(f"Tratamento concluído. {len(df)} registros prontos para importação.")
        
    except FileNotFoundError:
        print(f"Arquivo '{CSV_FILE}' não encontrado no diretório atual.")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
        sys.exit(1)

    print("Conectando ao PostgreSQL...")
    # Criando engine de conexão via SQLAlchemy
    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

    try:
        print(f"Inserindo dados na tabela '{TABLE_NAME}'...")
        # if_exists='replace' recria a tabela a cada execução
        # chunksize otimiza a inserção em lotes para volumes grandes
        df.to_sql(TABLE_NAME, engine, if_exists='replace', index=False, chunksize=10000)
        print(f"Importação concluída. Tabela '{TABLE_NAME}' atualizada com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar os dados no banco: {e}")

if __name__ == "__main__":
    main()