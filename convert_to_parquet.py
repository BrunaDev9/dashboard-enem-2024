import pandas as pd

# Arquivos a serem convertidos para o formato Parquet
arquivos = ['RESULTADOS_2024.csv', 'PARTICIPANTES_2024.csv']

for arquivo in arquivos:
    try:
        print(f"Lendo {arquivo}...")
        
        # Leitura com encoding Latin-1 e separador ';' (padrão INEP/ENEM)
        try:
            df = pd.read_csv(arquivo, sep=';', encoding='latin-1', low_memory=False)
        except:
            # Fallback: tenta separador padrão mantendo o encoding
            df = pd.read_csv(arquivo, encoding='latin-1', low_memory=False)
            
        nome_saida = arquivo.replace('.csv', '.parquet')
        
        print(f"Convertendo {arquivo} para Parquet...")
        # Compressão Snappy aplicada automaticamente pelo Pandas
        df.to_parquet(nome_saida, compression='snappy', index=False)
        
        print(f"Concluído: {nome_saida}")
        print("-" * 30)
        
    except Exception as e:
        print(f"Erro ao processar {arquivo}: {e}")

print("Conversão finalizada. Verifique os arquivos .parquet gerados.")