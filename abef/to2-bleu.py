import os
import nltk
import random
os.system("clear") # Clear last results in screen
 
# ---- main code - Parte um da frase -----------------------------------------

from nltk.translate.bleu_score import sentence_bleu
ref_google = "se você não encontra uma maneira de ganhar dinheiro enquanto dorme, você vai trabalhar até morrer"
ref_bing = "se você não encontrar uma maneira de ganhar dinheiro enquanto você dorme, você vai trabalhar até que você morrer"
ref_yandex = "se não encontrares uma maneira de ganhar dinheiro enquanto dormes, trabalharás até morreres"
candidate = ""
candidates = [
    "se não achar um jeito de fazer dinheiro enquanto dorme, trabalhará até morrer",
    "você irá trabalhar até morrer, se não achar um jeito de ganhar dinheiro enquanto dorme",
    "se tu não encontrares uma forma de ganhar dinheiro enquanto dormes, trabalharás até morrer",
    "se você não encontrar um caminho para fazer dinheiro enquanto você dorme, você trabalhará até você morrer",
    "se não encontrar você meio para criar dinheiro quando dorme você, trabalhar até morrer você irá",
    "se você não encontrar um jeito de ganhar dinheiro enquanto dorme, você vai trabalhar até morrer"
    ]
reference = [ref_google.split(' '),ref_bing.split(' '),ref_yandex.split(' ')]
#ref_text = ["the shirt","the shirt is tore","the shirt is black","a shirt can tear"]
#i = 0
#reference = []
#while i < len(ref_text):
#    reference.append(ref_text[i].split(' '))
#    i+=1

candidate = candidate.split(' ')
print("Referencia: {}".format(reference))
print("Original: "+' '.join(candidate))
i = 0
while i < len(candidates):
    candidate = candidates[i].split(' ')
    score = sentence_bleu(reference, candidate, weights=(1, 0, 0, 0))
    print("Candidato {}({}): {}".format(i,score,candidate))
    i+=1
