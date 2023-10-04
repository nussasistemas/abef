import os
import yaml
from data.class_weights import Class_Weights
from lib.abef import Abef

dict_pt_en = None
dict_en_pt = None
dict_main = None
ss_pt_en = None
sentence_o = None
candidates = None
t_o = []
source_language = None
target_language = None
class_penalties = ['i', 'j']
abef = None


def load_parameters(path):
    with open(path, 'r') as file:
        return yaml.full_load(file)


def main():
    global dict_pt_en, dict_en_pt, dict_main, ss_pt_en, sentence_o, source_language, target_language, abef

    sentences = ['a disposicao para se divertir']

    # Set the proper dictionary
    dict_source = load_parameters('./data/dictionary_pt_en.yml')

    if sentences[0].split(' ')[0] not in dict_source['words']:
        dict_source = load_parameters('./data/dictionary_en_pt.yml')

    new_ss = []
    for sentence in sentences:
        sentence_o = sentence.split(' ')
        structure = ""
        for word in sentence_o:
            classification = "|".join(dict_source['words'][word]['classification'])
            print("%s:%s" % (word, classification))
            structure = "%s%s" % (structure, classification)

        new_ss.append(structure)

    print(new_ss)


if __name__ == "__main__":
    main()
