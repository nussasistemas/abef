import os
import nltk
import random
os.system("clear") # Clear last results in screen
 
# ---- main code ------------------------------------------

from nltk.translate.bleu_score import sentence_bleu
ref_google = "the sleeve of the shirt tore"
ref_bing = "the shirt sleeve tore" # traduzi pelo site Systran Translate
ref_yandex = "shirt sleeve ripped"
candidate = ""
candidates = ["the tore sleeve","the collar has tear","the short sleeve rent","this shirt is torn","shirt sleeve the rent","the shirt sleeve tore"]
reference = [ref_google.split(' '),ref_bing.split(' '),ref_yandex.split(' ')]
ref_text = ["the shirt","the shirt is tore","the shirt is black","a shirt can tear","shirt sleeve"]
i = 0
reference = []
while i < len(ref_text):
    reference.append(ref_text[i].split(' '))
    i+=1

candidate = candidate.split(' ')
print("Referencia: {}".format(reference))
print("Original: "+' '.join(candidate))
i = 0
while i < len(candidates):
    candidate = candidates[i].split(' ')
    score = sentence_bleu(reference, candidate, weights=(1, 0, 0, 0))
    print("Candidato {}({}): {}".format(i,score,candidate))
    i+=1
