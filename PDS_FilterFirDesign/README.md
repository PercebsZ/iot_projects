
**Modelando um Filtro de Resposta ao Impulso Finita (Filtro FIR) com Python e integrado a um interface de usuário com Node-RED.**

Autores: Navid Salehi (back-end) e Tiago Sá (interface e integração)

Área do Conhecimento: Processamento Digital de Sinais (PDS)

Problema:

Elaborar uma interface gráfica para projeto de filtros FIR por janelamento em geral. A interface deverá permitir ao usuário a inserção/seleção dos seguintes parâmetros: 

a) Tipo de Filtro: passa-baixas, passa-altas, passa-faixas, rejeita-faixas;

b) Frequências de Corte: para filtros passa-baixas e passa-altas (FC1 e FC2); filtros passa-faixa e rejeita faixa (FC1, FC2, FS1, FS2);

c) Frequência de Amostragem;

d) Atenuação mínima na faixa de rejeição (-21 dB, -25 dB, -44 dB, -53 dB, -74 dB)

A partir dos parâmetros inseridos, a interface deverá apresentar ao usuário:

- Resposta em frequência do filtro (Decibéis x Frequência);

- Número de coeficientes do filtro.

De forma resumida, a modelagem do filtro foi feita utilizando a linguagem Python e a interface gráfica com Node-RED.

Ambos arquivos podem ser encontrados nesta pasta do github. 

Para finalizar, segue uma foto para ilustrar como ficou o projeto final:

![Ilustração Interface do Usuário](https://user-images.githubusercontent.com/49340230/98497096-840e7980-2219-11eb-9f5e-eabcf70ff43a.png)


Manaus-AM
08/11/2020

