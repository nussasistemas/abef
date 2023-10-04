---------------------
English
---------------------
## Round-trip Bilingual Evaluation

Project for Round-trip Bilingual Evaluation (RTBE)

This is a PhD project to design a novel method to evaluate translated texts based on pre-defined phrasal-structure.

How to install:
1. Clone the project folder

2. Install `requirements.txt` through 
```bash
pip install -r requirements.txt
```

3. Open the paste "abef" and next open archive python "to1-abef.py" for exemple

4. The open source code has areas that must be changed according to the user's preference such as:

	4.1 - "dicionario_pt_en" and "dicionario_en_pt" -> These dictionaries contain words and their translations. Modify them to add, remove, or update words as needed. For example, you can add new words and their translations or modify existing translations.

	4.2 - "frase_o" and "frase_t" -> You can replace these phrases with the ones you want to translate. Make sure that the phrases are in the correct language (Portuguese for the phrases in phrase_o and English for the phrases in phrase_t.

5. After performing the previous steps, run the program

6. Evaluation Criteria:

The program uses an evaluation criterion to determine the best translation. The criterion considers the following factors:

*Functional Equivalence Framework (FE): The program calculates the similarity of the FE of the original phrase and the FE of the target phrase.

*Keyword Matching: The program checks whether the key words in the original sentence have corresponding translations in the target sentence.

*Penalty for Word Repetition: The program penalizes sentences that have excessive word repetitions.

7. Finally the program calculates a score for each translation candidate based on these evaluations. The higher the score, the more suitable the translation is.

---------------------
Português
---------------------
## Avaliação bilingue de ida e volta

Projeto de Avaliação Bilingue Round-trip (RTBE)

Este é um projeto de doutoramento para conceber um novo método de avaliação de textos traduzidos com base em estruturas frasais pré-definidas.

Como instalar:
1. Clonar a pasta do projeto

2. Instalar o `requirements.txt` através do 
```bash
pip install -r requirements.txt
```

3. Abra a pasta "abef" e logo após, abra o arquivo python "to1-abef.py" por exemplo

4. O código fonte aberto tem áreas que devem ser alteradas de acordo com a preferência do utilizador, tais como:

	4.1 - "dicionario_pt_en" e "dicionario_en_pt" -> Estes dicionários contêm palavras e suas traduções. Modifique-os para adicionar, remover ou atualizar palavras conforme necessário. Por exemplo, pode acrescentar novas palavras e as suas traduções ou modificar as traduções existentes.

	4.2 - "frase_o" e "frase_t" -> Pode substituir estas frases pelas que pretende traduzir. Certifique-se de que as frases estão na língua correcta (português para as frases em frase_o e inglês para as frases em frase_t.

5. Depois de efetuar os passos anteriores, execute o programa

6. Critérios de avaliação:

O programa utiliza um critério de avaliação para determinar a melhor tradução. O critério considera os seguintes factores:

*Quadro de Equivalência Funcional (EF): O programa calcula a semelhança entre a FE da frase original e a FE da frase de destino.

*Correspondência de palavras-chave: O programa verifica se as palavras-chave da frase original têm traduções correspondentes na frase de destino.

*Penalização por Repetição de Palavras: O programa penaliza as frases que têm repetições excessivas de palavras.

7. Finalmente, o programa calcula uma pontuação para cada candidato a tradução com base nestas avaliações. Quanto maior for a pontuação, mais adequada é a tradução.

