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
OUTPUT_FILE = sys.argv[2]

adata = anndata.read_h5ad(DATA_PATH)

# sc.pl.umap(
#     adata,
#     color="cell_type",
#     size=8,
#     title="Human Immune Tissue UMAP",
# )

adata_obs_cols_to_keep = ["cell_type", "tissue", "batch_condition", "organism", "sex"]

# Create CSData object
arrow_ds, vocabulary = cs.CSData.adata_to_arrow(
    adata=adata, 
    random_state=SEED, 
    sentence_delimiter=' ',
    label_col_names=adata_obs_cols_to_keep
)

with open(OUTPUT_FILE, "w") as f:
    print("Keys:", file=f)
    print(adata.obs.keys(), file=f)
    print("", file=f)
    print("=================================", file=f)
    print("Sentences:", file=f)
    print(arrow_ds[0], file=f)



