Este script está no word que está sendo entregue

'''
Parte 2: Testes de Hipótese / Exercício 4
Dois grupos de estudantes foram submetidos a métodos de ensino diferentes. As notas de 20 alunos
do Grupo A e 20 alunos do Grupo B estão disponíveis. Use o teste t de Student para determinar se
há uma diferença significativa entre as médias das notas dos dois grupos. Considere α=0,05. Mostre
o código em Python para a realização do teste e interprete o resultado.

Objeto de Estudo: stats.shapiro / stats.levene / funções diversas Numpy

'''

#Globais

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Bibliotecas
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

#Conectar ao Google Drive
from google.colab import drive
drive.mount('/content/drive')
v_caminho_google_drive = '/content/drive/MyDrive/[MBA]/[Data Science Experience]/[Listas]/'

v_exercicio = '[Exercicio 04]/'

# Gerando a amostra aleatória.
np.random.seed(42)

# Gerando dados aleatórios/simulados para os dois grupos
v_grupo_a = np.random.normal(75, 8, 20) # Grupo A: média 75, desvio padrão 8
v_grupo_b = np.random.normal(80, 7, 20) # Grupo B: média 80, desvio padrão 7

# Limitando as notas entre 0 e 100
v_grupo_a = np.clip(v_grupo_a, 0, 100)
v_grupo_b = np.clip(v_grupo_b, 0, 100)

# Arredondando para uma casa decimal
v_grupo_a = np.round(v_grupo_a, 1)
v_grupo_b = np.round(v_grupo_b, 1)

# Criando um DataFrame para facilitar a visualização e análise
df_grupos = pd.DataFrame({
              'Grupo A': v_grupo_a,
              'Grupo B': v_grupo_b
})

# Exportando os dados
v_arq_notas_grupos = 'notas_grupos.csv';
df_grupos.to_csv((v_caminho_google_drive + v_exercicio + v_arq_notas_grupos), index=False)

#Funções  Estatísticas
print("Estatísticas:")
print("\nGrupo A:")
print(f"Média: {np.mean(v_grupo_a):.2f}")
print(f"Desvio Padrão: {np.std(v_grupo_a, ddof=1):.2f}")
print(f"Mínimo: {np.min(v_grupo_a):.2f}")
print(f"Máximo: {np.max(v_grupo_a):.2f}")

print("\nGrupo B:")
print(f"Média: {np.mean(v_grupo_b):.2f}")
print(f"Desvio Padrão: {np.std(v_grupo_b, ddof=1):.2f}")
print(f"Mínimo: {np.min(v_grupo_b):.2f}")
print(f"Máximo: {np.max(v_grupo_b):.2f}")

# Verificando a distribuição normal dos valores (pressuposto do teste t)
  #O pressuposto de normalidade no teste t refere-se à ideia de que os dados de cada grupo devem vir de uma distribuição normal (ou próxima de 
  #uma distribuição normal). 
  #Isso significa que os valores da variável dependente devem estar distribuídos simetricamente em torno da média, com a maioria dos valores 
  #concentrados perto do centro e poucos valores extremos. 
print("\nDistribuição normal dos valores (Stats.Shapiro):")
print(f"Grupo A: estatística={stats.shapiro(v_grupo_a)[0]:.4f}, p-valor={stats.shapiro(v_grupo_a)[1]:.4f}")
print(f"Grupo B: estatística={stats.shapiro(v_grupo_b)[0]:.4f}, p-valor={stats.shapiro(v_grupo_b)[1]:.4f}")

# Verificando a homogeneidade das variâncias (pressuposto do teste t)
  #A homogeneidade das variâncias, é um pressuposto fundamental em muitos testes estatísticos 
  #paramétricos, como o teste t de Student e a análise de variância (ANOVA). Significa que as variâncias (medida da dispersão dos dados) 
  #entre diferentes grupos ou amostras são aproximadamente iguais. Quando esse pressuposto é violado, a interpretação dos resultados do 
  #teste t pode ser comprometida, pois o erro padrão das médias pode ser distorcido. 
print("\nValidando a Dispersão dos Dados (Stats.Levene):")
print(f"Estatística={stats.levene(v_grupo_a, v_grupo_b)[0]:.4f}, p-valor={stats.levene(v_grupo_a, v_grupo_b)[1]:.4f}")

# Realizando o teste t de Student para dados aleatórios
v_alpha = 0.05
v_resultado_teste_t = stats.ttest_ind(v_grupo_a, v_grupo_b, equal_var=True)

print("\nResultado do Teste t de Student:")
print(f"Resultado do Teste t (Estatístico): {v_resultado_teste_t.statistic:.4f}")
print(f"Resultado do Teste t (Valor): {v_resultado_teste_t.pvalue:.4f}")
print(f"Disponibilidade: {len(v_grupo_a) + len(v_grupo_b) - 2}")
print(f"Alpha (α): {v_alpha}")

# Analisando o valor calculado
if v_resultado_teste_t.pvalue < v_alpha:
    print("Foram apresentados probabilidades estatísticas de diferenças entre as médias dos dois grupos.")
else:
    print("Não Foram apresentados probabilidades estatísticas de diferenças entre as médias dos dois grupos.")


# Criando visualizações

# Configuração para gráficos
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12

# Boxplot para comparar as distribuições
v_arq_comparacao_notas = 'boxplot_grupos'
plt.figure(figsize=(12, 6))
sns.boxplot(data=[v_grupo_a, v_grupo_b], width=0.5)
plt.xticks([0, 1], ['Grupo A', 'Grupo B'])
plt.ylabel('Notas')
plt.title('Comparação das Distribuições de Notas entre os Grupos')

plt.savefig((v_caminho_google_drive + v_exercicio + v_arq_comparacao_notas + '.png'), dpi=300, bbox_inches='tight')
plt.savefig((v_caminho_google_drive + v_exercicio + v_arq_comparacao_notas + '.pdf'))


# Histograma para visualizar a distribuição das notas
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.histplot(v_grupo_a, kde=True, color='blue')
plt.axvline(np.mean(v_grupo_a), color='red', linestyle='dashed', linewidth=2)
plt.title('Distribuição das Notas - Grupo A')
plt.xlabel('Notas')
plt.ylabel('Frequência')

plt.subplot(1, 2, 2)
sns.histplot(v_grupo_b, kde=True, color='green')
plt.axvline(np.mean(v_grupo_b), color='red', linestyle='dashed', linewidth=2)
plt.title('Distribuição das Notas - Grupo B')
plt.xlabel('Notas')
plt.ylabel('Frequência')

plt.tight_layout()
v_arq_histograma_notas = 'histograma_grupos'
plt.savefig((v_caminho_google_drive + v_exercicio + v_arq_histograma_notas + '.png'), dpi=300, bbox_inches='tight')
plt.savefig((v_caminho_google_drive + v_exercicio + v_arq_histograma_notas + '.pdf'))

# Gráfico de barras para comparar as médias
plt.figure(figsize=(10, 6))
v_medias = [np.mean(v_grupo_a), np.mean(v_grupo_b)]
v_erros = [stats.sem(v_grupo_a), stats.sem(v_grupo_b)]  # Erro padrão da média

plt.bar([0, 1], v_medias, yerr=v_erros, capsize=10, color=['blue', 'green'], alpha=0.7)
plt.xticks([0, 1], ['Grupo A', 'Grupo B'])
plt.ylabel('Média das Notas')
plt.title('Comparação das Médias das Notas entre os Grupos')

v_arq_barras_medias = 'barras_medias'
plt.savefig((v_caminho_google_drive + v_exercicio + v_arq_barras_medias + '.png'), dpi=300, bbox_inches='tight')
plt.savefig((v_caminho_google_drive + v_exercicio + v_arq_barras_medias + '.pdf'))

# Salvando os resultados em um arquivo de texto
v_arq_resultado_final = 'resultados_teste_t.txt'

with open((v_caminho_google_drive + v_exercicio + v_arq_resultado_final), 'w') as f:
    f.write("Resultados do Teste t de Student\n")
    f.write("===============================\n\n")

    f.write("Estatísticas:\n")
    f.write(f"Grupo A: Média = {np.mean(v_grupo_a):.2f}, Desvio Padrão = {np.std(v_grupo_a, ddof=1):.2f}\n")
    f.write(f"Grupo B: Média = {np.mean(v_grupo_b):.2f}, Desvio Padrão = {np.std(v_grupo_b, ddof=1):.2f}\n\n")

    f.write("Distribuição Normal (Stats.Shapiro):\n")
    f.write(f"Grupo A: estatística={stats.shapiro(v_grupo_a)[0]:.4f}, p-valor={stats.shapiro(v_grupo_a)[1]:.4f}\n")
    f.write(f"Grupo B: estatística={stats.shapiro(v_grupo_b)[0]:.4f}, p-valor={stats.shapiro(v_grupo_b)[1]:.4f}\n\n")

    f.write("Dispersão dos Dados (Stats.Levene):\n")
    f.write(f"Estatística={stats.levene(v_grupo_a, v_grupo_b)[0]:.4f}, p-valor={stats.levene(v_grupo_a, v_grupo_b)[1]:.4f}\n\n")

    f.write("Resultado do Teste t de Student:\n")
    f.write(f"Resultado do Teste t (Estatístico):: {v_resultado_teste_t.statistic:.4f}\n")
    f.write(f"Resultado do Teste t (Valor): {v_resultado_teste_t.pvalue:.4f}\n")
    f.write(f"Disponibilidade: {len(v_grupo_a) + len(v_grupo_b) - 2}\n")
    f.write(f"Alpha (α): {v_alpha}\n\n")


    if v_resultado_teste_t.pvalue < v_alpha:
        f.write("Foram apresentados probabilidades estatísticas de diferenças entre as médias dos dois grupos.\n")
    else:
        f.write("Não foram apresentados probabilidades estatísticas de diferenças entre as médias dos dois grupos.\n")

print("\nFim da Análise. Os resultados foram salvos em arquivos.")