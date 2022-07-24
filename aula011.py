"""
            CORES NO TERMINAL
------------------------------------------------------------
- no python existe varias formas de fazer a mesma coisa     |
- ANSI - escape sequence                                    |
    sempre começa com '\' e depois vem o codigo             |
REPRESENTANDDO EM PYTHON                                    |
    \033[m - entre o [ e a letra 'm', vem o codigo da cor   |
\033[style; text; back m                                    |
------------------------------------------------------------

------------------------------------------------------------
STYLE             TEXT             BACK                     |
------------------------------------------------------------
0 NONE          |30 - BRANCO    | 40 - BRANCO               |
1 BOLD          |31 - VERMELHO  | 41 - VERMELHO             |
4 UNDERLINE     |32 - VERDE     | 42 - VERDE                |
7 NEGATIVE      |33 - AMARELO   | 43 - AMARELO              |
                |34 - AZUL      | 44 - AZUL                 |
                |35 - MAJENTA   | 45 - MAJENTA              |
                |36 - CIANO     | 46 - CIANO                |
                |37 - CINZA     | 47 - CINZA                |
------------------------------------------------------------
EXEMPLO:
        \033[0;33;44m - TEXTO AMARELO COM FUNDO AZUL
*BOLD - negrito
*UNDERLINE - sublinhado
*NEGATIVE - inversão de cor
_______________________
\033[0;30;41m
\033[4;33;44m
\033[1;35;43m
\033[30;42m
\033[m
\033[7;30m
_______________________
"""
