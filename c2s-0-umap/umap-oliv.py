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

print(f"Formato do dataset: {X.shape}")
print(f"Número de indivíduos: {len(np.unique(y))}")
print(f"Número de imagens por indivíduo: {X.shape[0] // len(np.unique(y))}")

# Criar uma ocorrência de UMAP com parâmetros defaults
redutor = umap.UMAP(random_state=42)

# Transformar os dados
embedding = redutor.fit_transform(X)

# Gerar um mapa de cores para 40 classes
colors = cm.get_cmap('hsv', 40)  

# Visualizar
plt.figure(figsize=(12, 10))
scatter = plt.scatter(embedding[:, 0], embedding[:, 1], c=y,
                    cmap=colors, s=50, alpha=0.8, edgecolors='black', linewidth=0.5)
plt.colorbar(scatter, label='Person ID', ticks=np.arange(0, 40, 5))
plt.title('UMAP: Projeção de faces de Olivetti')
plt.xlabel('UMAP 1')
plt.ylabel('UMAP 2')
plt.grid(True, alpha=0.3)
plt.show()

