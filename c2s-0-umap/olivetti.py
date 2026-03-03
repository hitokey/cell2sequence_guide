import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.datasets import fetch_olivetti_faces
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import umap
import warnings
warnings.filterwarnings('ignore')

# Carregue as faces de Olivetti
faces = fetch_olivetti_faces(shuffle=True, random_state=42)
X = faces.data
y = faces.target

# Note que Python (e todas as linguagens de script)
# não passa de uma forma complicada de chamar
# programas escritos em C, Fortran, Java e Lisp.
# O script-writer de Python sequer sabe abrir um
# arquivo de dados. Chama um programa que já
# sabe onde o arquivo está. Outras linguagens
# de script que funcionam assim são R e Matlab.

print(f"Formato do dataset: {X.shape}")
print(f"Número de indivíduos: {len(np.unique(y))}")
print(f"Número de imagens por indivíduo: {X.shape[0] // len(np.unique(y))}")

# Pequena amostra das faces
fig, axes = plt.subplots(3, 2, figsize=(10, 4))
for i, ax in enumerate(axes.flat):
   ax.imshow(X[i].reshape(64, 64), cmap='gray')
   ax.set_title(f'Pessoa {y[i]}')
   ax.axis('off')
plt.suptitle('Amostras de faces do Dataset de Python')
plt.tight_layout()
plt.show()

