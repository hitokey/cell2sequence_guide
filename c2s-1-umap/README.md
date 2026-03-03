
# Converting H5AD Single-Cell RNA-seq Data into Sentences

This folder contains the following files:

```
immune_tissue_10cells.h5ad
pancreas.h5ad

sentence.py
sent.py
keys.py

```

The following command translates `immune_tissue_10cells.h5ad` into a sentence stored in the file `outupt-immune.txt`:

```
python sentence.py immune_tissue_10cells.h5ad output-immune.txt
```

In the `sentence.py` script, you must specify the column keys that the researcher wants to include.
The `keys.py` script lists all available keys:

```
(cell) ~/c2s-yale/cell2sequence_guide/c2s-1-umap$ python keys.py immune_tissue_10cells.h5ad 
Keys:
Index(['cell_id', 'cell_type', 'tissue', 'donor_id', 'sample_id',
       'batch_condition', 'organism', 'assay', 'disease', 'sex',
       'self_reported_ethnicity', 'development_stage', 'orig_filename',
       'rahul_tissue_categ'],
      dtype='object')
```

The `sent.py` script creates sentences from files such as `pancreas.h5ad`, as shown below:

```
(cell) ~/c2s-yale/cell2sequence_guide/c2s-1-umap$ python sent.py pancreas.h5ad output-pancreas.txt
100%|██████████████████████| 1387/1387 [00:00<00:00, 5695.26it/s]
```

The files `immune-output.txt` and `pancreas-sentence.output` contain the outputs produced by `sentence.py` and `sent.py`, respectively.


