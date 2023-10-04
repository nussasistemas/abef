import os
import yaml
from data.class_weights import Class_Weights
from lib.abef import Abef
from lib.ga_to1 import ga

dict_pt_en = None
dict_target = None
dict_main = None
ss_sl_tl = None
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
    var_test = abef.get_ss_string(t_o)
    ss_sl_tl = abef.get_ss_target(abef.get_ss_string(t_o), dict_ss_sl_tl)
    ss_t = abef.get_ss_string(t_t)
    if len(ss_sl_tl) > 0:
        ss = abef.get_nearest_ss(ss_t, ss_sl_tl)
        fx_ss = abef.aval_ss(ss_t, ss_sl_tl[ss])
        return abef.aval_sentence(t_t, t_o, ss_sl_tl[ss], source_language, fx_ss)
    return 0


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
            evaluation = 1 - evaluate(t_o, candidate, abef, source_language, dict_main, ss_sl_tl)
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
    global dict_pt_en, dict_target, dict_main, ss_sl_tl, sentence_o, source_language, target_language, abef
    """
    
        Troque abaixo a frase que deseja traduzir
    
    """
    sentence_o = 'you can try to create consistency without having the appropriate beliefs and attitudes'.split(' ')
    source_language = 'en'
    target_language = 'pt'
    language_pair = '%s_%s' % (source_language, target_language)
    dict_source = load_parameters('./data/dictionary_%s_%s.yml' % (source_language, target_language))
    dict_target = load_parameters('./data/dictionary_%s_%s.yml' % (target_language, source_language))
    ss_sl_tl = load_parameters('./data/ss_%s.yml' % language_pair)
    dict_main = filter_dictionary(dict_target['words'], sentence_o)

    for word in sentence_o:
        t_o.append(dict_source['words'][word])

    abef = Abef(dict_source['words'], dict_target['words'], source_language, target_language, Class_Weights,
                class_penalties)

    individuals = 20
    genes = len(sentence_o)+1
    ger = 10000
    max_number = len(dict_source)
    results = ga(individuals, genes, ger, max_number, f_aval, get_sentence)

    results_path = os.path.basename(__file__)
    results_path = results_path.replace("tradutor", "results").replace(".py", ".csv")

    with open('./results/%s' % results_path, 'w') as file:
        for result in results:
            file.write("%d, %.10f\n" % (result[0], result[1]))


if __name__ == "__main__":
    main()
