import os

os.system("clear")  # Clear last results in screen

# ---- main code ------------------------------------------
import nltk
nltk.download('wordnet')

from nltk.translate.meteor_score import meteor_score

references = [
    "Ahead of us stretches the future like a road lost in the distance"
    "Ahead of us extends the future as a road that is lost in the distance"
]

candidates = [
    "Ahead of you stretches your future like a road leading into the distance."
    ]

i = 1
for candidate in candidates:
    score = meteor_score(references, candidate)
    print("Candidate {}: ({}): {}".format(i, score, candidate))
    i += 1
