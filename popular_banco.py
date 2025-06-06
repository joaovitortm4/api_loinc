import pandas as pd
import sqlite3

# Caminho para o arquivo CSV
csv_file = 'LoincTableCore.csv'

# Nome da tabela no SQLite
table_name = 'dados'

# Conectar ao banco de dados (cria se não existir)
conn = sqlite3.connect('banco_loinc.db')

# Ler CSV usando pandas
df = pd.read_csv(csv_file)

# Exportar para SQLite
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Fechar conexão
conn.close()

print("Importacao concluída!")
