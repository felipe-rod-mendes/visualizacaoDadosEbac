import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Importação das bibliotecas realizada com sucesso!")

# importar dados do arquivo
file_patch = "dados/clientes-v3-preparado.csv"
df = pd.read_csv(file_patch)
print(f"\nArquivo {file_patch} carregado com sucesso!")

# teste de gráfico
plt.hist(df['salario'])
plt.show()
