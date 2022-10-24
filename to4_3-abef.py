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

    ss_sl_tl = abef.get_ss_target(abef.get_ss_string(t_o), dict_ss_sl_tl)
    ss_t = abef.get_ss_string(t_t)

    if len(ss_sl_tl) > 0:
        ss = abef.get_nearest_ss(ss_t, ss_sl_tl)
        fx_ss = abef.aval_ss(ss_t, ss_sl_tl[ss])
        return abef.aval_sentence(t_t, t_o, ss_sl_tl[ss], source_language, fx_ss)
    return 0


def main():
    global dict_pt_en, dict_target, dict_main, ss_sl_tl, sentence_o, source_language, target_language, abef
    """

        Troque abaixo a frase que deseja traduzir

    """
    sentences = ['it can be very difficult to change your perspective to one where you',]
    candidates = ['é muito difícil mudar',
                  ]

    source_language = 'en'
    target_language = 'pt'
    language_pair = '%s_%s' % (source_language, target_language)
    dict_source = load_parameters('./data/dictionary_%s_%s.yml' % (source_language, target_language))
    dict_target = load_parameters('./data/dictionary_%s_%s.yml' % (target_language, source_language))
    ss_sl_tl = load_parameters('./data/ss_%s.yml' % language_pair)
    i = 0

    f_abef = []
    for candidate in candidates:
        t_o = []
        sentence_o = sentences[i].split(' ')

        for word in sentence_o:
            t_o.append(dict_source['words'][word])

        abef = Abef(dict_source['words'], dict_target['words'], source_language, target_language, Class_Weights,
                    class_penalties)

        fx = evaluate(t_o, candidate, abef, source_language, dict_target['words'], ss_sl_tl)
        f_abef.append(fx)
        print("Score: %s \t Candidate: %s" % (fx, candidate))

        i += 1

    print("F_AVAL: %s" % (sum(f_abef)/len(candidates)))


if __name__ == "__main__":
    main()
