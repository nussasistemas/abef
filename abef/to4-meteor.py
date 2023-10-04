import os

os.system("clear")  # Clear last results in screen

# ---- main code ------------------------------------------
import nltk
nltk.download('wordnet')

from nltk.translate.meteor_score import meteor_score

references = [
    "seu estado de espírito é um subproduto de suas crenças e atitudes. você pode tentar criar consistência sem ter as crenças e atitudes apropriadas, mas seus resultados não serão diferentes do que se você tentar ser feliz quando não estiver se divertindo. quando você não está se divertindo, pode ser muito difícil mudar sua perspectiva para uma em que, de repente, comece a se divertir"
    "seu estado mental é um subproduto de suas crenças e atitudes. você pode tentar criar consistência sem ter as crenças e atitudes apropriadas, mas seus resultados não serão diferentes do que se você tentar ser feliz quando você não está se divertindo. quando você não está se divertindo, pode ser muito difícil mudar sua perspectiva para uma em que você, de repente, começa a se divertir"
    "o estado mental é um subproduto das convicções e das atitudes. podemos tentar ser consistentes sem ter as convicções e atutides adequadas, mas os resultados não serão diferentes do que tentar divertir-se quando não está feliz. quando não está feliz, é muito difícil mudar subitamente a disposição para se divertir."
]

candidates = [
    "o estado mental é um subproduto das convicções e das atitudes. podemos tentar ser consistentes sem ter as convicções e atitudes adequadas, mas os resultados não serão diferentes do que tentar divertir quando não está feliz. quando não está feliz, é muito dificil mudar subitamente a disposicao para se divertir"
    ]

i = 1
for candidate in candidates:
    score = meteor_score(references, candidate)
    print("Candidate {}: ({}): {}".format(i, score, candidate))
    i += 1
