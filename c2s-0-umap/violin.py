# Python built-in libraries
import os
import random
from collections import Counter
import sys

# Third-party libraries
import numpy as np

# Single-cell libraries
import anndata
import scanpy as sc
from collections import Counter

SEED = 1234
random.seed(SEED)
np.random.seed(SEED)

DATA_PATH = sys.argv[1]

adata = anndata.read_h5ad(DATA_PATH)
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)

adata.var["mt"] = adata.var_names.str.startswith("MT-")
sc.pp.calculate_qc_metrics(
    adata, qc_vars=["mt"], percent_top=None, log1p=False, inplace=True
)
adata = adata[adata.obs.n_genes_by_counts < 6000, :]
adata = adata[adata.obs.pct_counts_mt < 50, :].copy()
sc.pp.normalize_total(adata)
# Lop1p transformation with base 10
sc.pp.log1p(adata, base=10)

sc.tl.pca(adata)
sc.pp.neighbors(adata, n_neighbors=8) 
sc.tl.umap(adata)

sc.pl.umap(
    adata,
    color="cell_type",
    size=100,
    title="Human Immune Tissue UMAP",
)

