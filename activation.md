# Activation after creation of the cell sandbox

```bash
~/c2s/cell2sentence$ source ~/miniconda3/bin/activate

(base) ~/c2s-yale/cell2sentence$ conda activate cell
```

An option is simply source the script `xact.src` as shown below.

```bash
source xact.src
```

Source the script `ydeact.src` to deactivate:

```bash
source ydeact.src
```

## Only at the first time 

```bash
(cell) ~/c2s-yale$ git clone https://github.com/SiYangming/cell2sentence-ft.git

(cell) ~/c2s-yale$ cd cell2sentence

(cell) ~/c2s-yale/cell2sentence$ pip install .
```

## First test

```bash
(cell) ~/c2s-yale/cell2sentence$ cd ..
(cell) ~/c2s-yale$ ls
cell2sentence  cell2sequence_guide  gitcmds.rd  token.github
(cell) ~/c2s-yale$ cd cell2sequence_guide/
(cell) ~/c2s-yale/cell2sequence_guide$ ls
activation.md  c2s-0-umap  image  README.md  ssh-key-for-github.md
(cell) ~/c2s-yale/cell2sequence_guide$ cd c2s-0-umap/
(cell) ~/c2s-yale/cell2sequence_guide/c2s-0-umap$ ls
img  olivetti.py  pancreas.h5ad  README.md  umap-oliv.py violin.py
(cell) ~/c2s-yale/cell2sequence_guide/c2s-0-umap$ python violin.py pancreas.h5ad
```

## Resultado

![UMAP de células de pâncreas](c2s-0-umap/img/umap-pancreas-h5ad.jpg)

