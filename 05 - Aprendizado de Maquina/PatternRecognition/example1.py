import numpy as np
import matplotlib.pyplot as plt

# Gerando dados de treinamento
np.random.seed(0)
N = 10
x_train = np.linspace(0, 1, N)
t_train = np.sin(2 * np.pi * x_train) + np.random.normal(scale=0.1, size=N)

# Curva da função sin(2πx)
x_curve = np.linspace(0, 1, 100)
y_curve = np.sin(2 * np.pi * x_curve)

# Plotando o gráfico
plt.figure(figsize=(8, 6))
plt.scatter(x_train, t_train, color='blue', label='Dados de Treinamento')
plt.plot(x_curve, y_curve, color='green', label='sin(2πx)')
plt.xlabel('x')
plt.ylabel('t')
plt.title('Dados de Treinamento e Função sin(2πx)')
plt.legend()
plt.grid(True)
plt.show()
