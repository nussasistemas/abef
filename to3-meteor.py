import os

os.system("clear")  # Clear last results in screen

# ---- main code ------------------------------------------
import nltk
nltk.download('wordnet')

from nltk.translate.meteor_score import meteor_score

references = [
    "the shirt",
    "the shirt is tore",
    "the shirt is black",
    "a shirt can tear",
    "shirt sleeve"
]

candidates = [
    "the tore sleeve",
    "the collar has tear",
    "the short sleeve rent",
    "this shirt is torn",
    "shirt sleeve the rent",
    "the shirt sleeve tore"
]

i = 1
for candidate in candidates:
    score = meteor_score(references, candidate)
    print("Candidate {}: ({}): {}".format(i, score, candidate))
    i += 1
