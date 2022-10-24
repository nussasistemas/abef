import os
import yaml
from data.class_weights import Class_Weights
from lib.abef import Abef
from lib.ga_to1 import ga

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


def evaluate(t_o, candidate, abef, source_language, dictionary, dict_ss_sl_tl):
    sentence_t = candidate.split(' ')
    t_t = []

    for word in sentence_t:
        t_t.append(dictionary[word])

    ss_sl_tl = abef.get_ss_target(abef.get_ss_string(t_o), dict_ss_sl_tl)
    ss_t = abef.get_ss_string(t_t)
    ss = abef.get_nearest_ss(ss_t, ss_sl_tl)
    fx_ss = abef.aval_ss(ss_t, ss_sl_tl[ss])
    return abef.aval_sentence(t_t, t_o, ss_sl_tl[ss], source_language, fx_ss)


def f_aval(candidates_vector):
    fx = []

    for candidate_vector in candidates_vector:
        candidate_list = list(map(round, candidate_vector))

        if min(candidate_list) >= 0 and max(candidate_list) < len(dict_main):
            words = []
            candidate = []

            for key in dict_main:
                words.append(key)

            for position in candidate_list:
                candidate.append(words[position])

            candidate = ' '.join(candidate)
            evaluation = 1 - evaluate(t_o, candidate, abef, source_language, dict_main, ss_pt_en)
            fx.append(evaluation)
        else:
            fx.append(float('inf'))

    return fx


def get_sentence(candidate_vector):
    words = []
    candidate = []
    candidate_list = list(map(round, candidate_vector[:-1]))

    for key in dict_main:
        words.append(key)

    for position in candidate_list:
        candidate.append(words[position])

    return ' '.join(candidate)


def filter_dictionary(dictionary, words):
    new_dict = {}
    for word in dictionary:
        for translate in dictionary[word]['translations']:
            if translate in words:
                new_dict[word] = dictionary[word]
                break

    return new_dict


def main():
    global dict_pt_en, dict_en_pt, dict_main, ss_pt_en, sentence_o, source_language, target_language, abef

    dict_pt_en = load_parameters('./data/dictionary_pt_en.yml')
    dict_en_pt = load_parameters('./data/dictionary_en_pt.yml')
    ss_pt_en = load_parameters('./data/ss_pt_en.yml')
    sentence_o = 'o cavalo é branco'.split(' ')
    source_language = 'pt'
    target_language = 'en'

    dict_main = filter_dictionary(dict_en_pt['words'], sentence_o)

    for word in sentence_o:
        t_o.append(dict_pt_en['words'][word])

    abef = Abef(dict_pt_en['words'], dict_en_pt['words'], source_language, target_language, Class_Weights,
                class_penalties)

    individuals = 10
    genes = len(sentence_o)
    ger = 1000
    max_number = len(dict_pt_en)
    results = ga(individuals, genes, ger, max_number, f_aval, get_sentence)

    results_path = os.path.basename(__file__)
    results_path = results_path.replace("tradutor", "results").replace(".py", ".csv")

    with open('./results/%s' % results_path, 'w') as file:
        for result in results:
            file.write("%d, %.10f\n" % (result[0], result[1]))


if __name__ == "__main__":
    main()
