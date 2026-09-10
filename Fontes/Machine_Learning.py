"""
Vamos imaginar que queremos prever se uma pessoa vai 
comprar um produto com base na idade e na renda.
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Criando os Dados
df = pd.DataFrame({
    'idade': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    'renda': [2000, 2500, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    'comprou': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
})

print(df)
print()

# Separando os dados em variáveis independentes (X) e dependentes (y)
X = df[['idade', 'renda']]
y = df['comprou']

# Dividindo os dados em conjunto de treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

"""
X_treino + y_treino → ensinam o modelo
X_teste → usado para fazer previsões
y_teste → usado para conferir se acertou
"""

# Criando o modelo de árvore de decisão
modelo = DecisionTreeClassifier(random_state=42)

# Treinando o modelo
modelo.fit(X_treino, y_treino)

# Fazendo previsões
previsoes = modelo.predict(X_teste)

# Comparar previsão com resultado real
print("Resultados Reais:", y_teste.values)
print("Previsão........:", previsoes)

# Calculando a acurácia do modelo
acuracia = accuracy_score(y_teste, previsoes)

print("Acurácia:", acuracia)
print()

# Prever uma nova pessoa
nova_pessoa = pd.DataFrame({
    'idade': [42],
    'renda': [5500]
})

resultado = modelo.predict(nova_pessoa)

print("Previsão para nova pessoa:", resultado)