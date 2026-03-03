# UMAP of h5ad files

Para desenhar UMAPs, você vai precisar de arquivos no formato h5ad contendo 'single-cell RNA sequences'. Eis onde encontrá-los:

[https://cellxgene.cziscience.com/datasets](https://cellxgene.cziscience.com/datasets)

É preciso escolher arquivos pequenos, com poucas células. Do contrário, derruba o computador. Para executar no meu computador, costumo escolher arquivos com menos de 10 mil células. Agora, vamos começar com o seguinte tutorial:

`c2s_tutorial_0_data_preparation.ipynb`

Esse tutorial ensina a fazer UMAP. No seu github, faça um tutorial sobre UMAP, que é a coisa mais básica da medicina de precisão. Vamos fazer um teste. Então, vamos para a página abaixo.

[https://cellxgene.cziscience.com/datasets](https://cellxgene.cziscience.com/datasets)

Façamos o download do arquivo intitulado 'Sub UMAP of the pancreas'. Chamemos o arquivo de 'pancreas.h5ad'. Para fazer o UMAP, escrevi o programa em Python anexo para construí-lo. Eis como executei o programa:

`(cell) ~/lixo$ python violin.py pancreas.h5ad`

O UMAP ficou assim:

![UMAP de células de pâncreas](img/umap-pancreas-h5ad.jpg)

