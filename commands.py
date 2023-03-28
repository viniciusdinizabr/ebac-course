# código de geração do gráfico 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Lendo o arquivo csv e transformando para DataFrame
df = pd.read_csv('gasolina.csv')

# Gerando o gráfico de linha
grafico = sns.lineplot(data=df, x='dia', y='venda', errorbar=None).set(title="Preço médio vs Dia")

# Salvando o arquivo em png
plt.savefig('gasolina.png')