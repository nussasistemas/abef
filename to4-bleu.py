import os
import nltk
import random
os.system("clear") # Clear last results in screen
 
# ---- main code - Parte um da frase -----------------------------------------

from nltk.translate.bleu_score import sentence_bleu
ref_google = "seu estado de espírito é um subproduto de suas crenças e atitudes. você pode tentar criar consistência sem ter as crenças e atitudes apropriadas, mas seus resultados não serão diferentes do que se você tentar ser feliz quando não estiver se divertindo. quando você não está se divertindo, pode ser muito difícil mudar sua perspectiva para uma em que, de repente, comece a se divertir"
ref_bing = "seu estado mental é um subproduto de suas crenças e atitudes. você pode tentar criar consistência sem ter as crenças e atitudes apropriadas, mas seus resultados não serão diferentes do que se você tentar ser feliz quando você não está se divertindo. quando você não está se divertindo, pode ser muito difícil mudar sua perspectiva para uma em que você, de repente, começa a se divertir"
ref_yandex = "seu estado de espírito é um subproduto de suas crenças e atitudes. podeis tentar criar consistência sem ter as crenças e atitudes apropriadas, mas os vossos resultados não serão diferentes do que se tentardes ser felizes quando não estais a divertir-vos. quando você não está se divertindo, pode ser muito difícil mudar sua perspectiva para uma onde você, de repente, começar a se divertir"
ref_reverso = "seu estado mental é um subproduto de suas crenças e atitudes. você pode tentar criar consistência sem ter as crenças e atitudes apropriadas, mas seus resultados não serão diferentes do que se você tentar ser feliz quando você não está se divertindo. quando você não está se divertindo, pode ser muito difícil mudar sua perspectiva para uma onde você, de repente, começa a se divertir"
ref_humana = "o estado mental é um subproduto das convicções e das atitudes. podemos tentar ser consistentes sem ter as convicções e atutides adequadas, mas os resultados não serão diferentes do que tentar divertir-se quando não está feliz. quando não está feliz, é muito difícil mudar subitamente a disposição para se divertir"

candidate = ""
candidates = ["o estado mental é um subproduto das convicções e das atitudes. podemos tentar ser consistentes sem ter as convicções e atitudes adequadas, mas os resultados não serão diferentes do que tentar divertir quando não está feliz. quando não está feliz, é muito dificil mudar subitamente a disposicao para se divertir."]
reference = [
    ref_google.split(' '),
    ref_bing.split(' '),
    ref_humana.split(' ')
]

candidate = candidate.split(' ')
print("Referencia: {}".format(reference))
print("Original: "+' '.join(candidate))
i = 0
while i < len(candidates):
    candidate = candidates[i].split(' ')
    score = sentence_bleu(reference, candidate, weights=(1, 1, 1, 1))
    print("Candidato {}({}): {}".format(i, score, candidate))
    i += 1
