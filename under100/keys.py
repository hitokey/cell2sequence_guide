# Python built-in libraries
import os
import random
from collections import Counter
import sys

# Third-party libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from tqdm import tqdm

# Single-cell libraries
import anndata
import scanpy as sc

# Cell2Sentence imports
import cell2sentence as cs
from cell2sentence.utils import benchmark_expression_conversion, reconstruct_expression_from_cell_sentence
              
SEED = 1234
random.seed(SEED)
np.random.seed(SEED)

DATA_PATH = sys.argv[1]

adata = anndata.read_h5ad(DATA_PATH)


print("Keys:")
print(adata.obs.keys())


