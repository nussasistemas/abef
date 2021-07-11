import os

os.system("clear")  # Clear last results in screen

# ---- main code ------------------------------------------
import nltk
nltk.download('wordnet')

from nltk.translate.meteor_score import meteor_score

references = [
    "se você não encontra uma maneira de ganhar dinheiro enquanto dorme, você vai trabalhar até morrer"
    "se você não encontrar uma maneira de ganhar dinheiro enquanto você dorme, você vai trabalhar até que você morrer"
    "se não encontrares uma maneira de ganhar dinheiro enquanto dormes, trabalharás até morreres"
]

candidates = [
    "se não achar um jeito de fazer dinheiro enquanto dorme, trabalhará até morrer",
    "você irá trabalhar até morrer, se não achar um jeito de ganhar dinheiro enquanto dorme",
    "se tu não encontrares uma forma de ganhar dinheiro enquanto dormes, trabalharás até morrer",
    "se você não encontrar um caminho para fazer dinheiro enquanto você dorme, você trabalhará até você morrer",
    "se não encontrar você meio para criar dinheiro quando dorme você, trabalhar até morrer você irá",
    "se você não encontrar um jeito de ganhar dinheiro enquanto dorme, você vai trabalhar até morrer"
    ]

i = 1
for candidate in candidates:
    score = meteor_score(references, candidate)
    print("Candidate {}: ({}): {}".format(i, score, candidate))
    i += 1
