import os
import nltk
import random
os.system("clear") # Clear last results in screen

# ---- main code ------------------------------------------

from nltk.translate.bleu_score import sentence_bleu
ref_google = "the white horse's coat is white"
ref_bing = "the white horse hair is white"
ref_yandex = "white horse hair is white"
candidate = "the white horse"
candidates = ["the white horse","the chicken is white","the the the the","this horse is black","white is horse the","the horse is white"]
reference = [ref_google.split(' '),ref_bing.split(' '),ref_yandex.split(' ')]
#reference = [['the', 'white', 'small', 'test']]
ref_text = ["an white cow","the horse is white","the horse is alive","an cow is falling"]
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

#random.shuffle(candidate)
#print("Embaralhado: "+' '.join(candidate))
#score = sentence_bleu(reference, candidate, weights=(1, 0, 0, 0))
#print(score)[i]