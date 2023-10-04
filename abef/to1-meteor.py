import os

os.system("clear")  # Clear last results in screen

# ---- main code ------------------------------------------
import nltk
nltk.download('wordnet')

from nltk.translate.meteor_score import meteor_score

candidates = ["the white horse", "the chicken is white", "the the the the", "this horse is black", "white is horse the",
              "the horse is white"]
references = ["an white cow", "the horse is white", "the horse is alive", "an cow is falling"]

i = 1
for candidate in candidates:
    score = meteor_score(references, candidate)
    print("Candidate {}: ({}): {}".format(i, score, candidate))
    i += 1
