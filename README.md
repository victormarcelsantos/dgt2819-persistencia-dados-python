# DGT2819 - Persistência de dados com Python

Trabalho prático: glossário de palavras ordenadas a partir de arquivos de texto.

## Arquivos

- `array.sort.py`, `bubble.sort.py`, `selection.sort.py`: microatividades de ordenação
- `ler.txt.py`, `escrever.txt.py`: microatividades de leitura e escrita de arquivos
- `kdd_comparativo.py`: compara Bubble Sort, Selection Sort e sort nativo
- `kdd.py`: versão final, que lê `documento.txt` e grava `palavras_ordenadas.txt`

## Comparação de desempenho

| Execução | Bubble Sort | Selection Sort | Sort nativo |
|---|---|---|---|
| 1 | 0,262348 s | 0,127610 s | 0,000317 s |
| 2 | 0,238834 s | 0,121269 s | 0,000320 s |
| 3 | 0,240457 s | 0,127157 s | 0,000463 s |
| Média | 0,247213 s | 0,125345 s | 0,000367 s |

## Conclusão

O `sort()` nativo do Python foi o método de melhor desempenho, cerca de
340 vezes mais rápido que o Selection Sort e 670 vezes mais rápido que o
Bubble Sort. Por isso, foi o método mantido no `kdd.py` final.

## Como executar

```
python kdd.py
```