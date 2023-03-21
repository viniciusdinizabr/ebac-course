# código de geração do gráfico 

import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo csv e transformando para DataFrame
df = pd.read_csv('gasolina.csv')

# Gerando o gráfico de linha
lines = df.plot.line(x='dia', y='venda')

# Salvando o arquivo em png
plt.savefig('gasolina.png')