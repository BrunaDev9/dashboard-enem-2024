import pandas as pd

# Lista dos arquivos que vamos converter
arquivos = ['RESULTADOS_2024.csv', 'PARTICIPANTES_2024.csv']

for arquivo in arquivos:
    try:
        print(f"Lendo {arquivo}... Isso pode demorar (o de 1.6GB exige paciência!).")
        
        # Tentando ler com Latin-1 e separador ';' (comum no ENEM)
        try:
            df = pd.read_csv(arquivo, sep=';', encoding='latin-1', low_memory=False)
        except:
            # Se falhar o separador, tenta o padrão com a mesma codificação
            df = pd.read_csv(arquivo, encoding='latin-1', low_memory=False)
            
        nome_saida = arquivo.replace('.csv', '.parquet')
        
        print(f"Convertendo {arquivo} para Parquet...")
        # Salvando em Parquet (o Pandas cuidará da compressão Snappy automaticamente)
        df.to_parquet(nome_saida, compression='snappy', index=False)
        
        print(f"Sucesso! Gerado: {nome_saida}")
        print("-" * 30)
        
    except Exception as e:
        print(f"Erro ao processar {arquivo}: {e}")

print("Processo finalizado! Agora verifique o tamanho dos arquivos .parquet no terminal.")