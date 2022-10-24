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
class_penalties = []
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
    sentences = ['your state of mind is a by-product of your beliefs and attitudes',
                 'you can try to create consistency without having the appropriate beliefs and attitudes',
                 'but your results will not be any different than if you try to be happy when you are not having fun',
                 'when you are not having fun',
                 'it can be very difficult to change your perspective to one where you all of a sudden start enjoying yourself']
    candidates = ['o estado mental é um subproduto das convicções e das atitudes',
                  'podemos tentar ser consistentes sem ter as convicções e atitudes adequadas',
                  'mas os resultados não serão diferentes do que tentar divertir quando não está feliz',
                  'quando não está feliz',
                  'é muito difícil mudar subitamente a disposicao para se divertir']

    source_language = 'en'
    target_language = 'pt'
    language_pair = '%s_%s' % (source_language, target_language)
    dict_source = load_parameters('./data/dictionary_%s_%s.yml' % (source_language, target_language))
    dict_target = load_parameters('./data/dictionary_%s_%s.yml' % (target_language, source_language))
    ss_sl_tl = load_parameters('./data/ss_%s.yml' % language_pair)
    i = 0

    f_abef = []
    f_weight = []
    for candidate in candidates:
        t_o = []
        sentence_o = sentences[i].split(' ')

        for word in sentence_o:
            t_o.append(dict_source['words'][word])

        abef = Abef(dict_source['words'], dict_target['words'], source_language, target_language, Class_Weights,
                    class_penalties)

        fx = evaluate(t_o, candidate, abef, source_language, dict_target['words'], ss_sl_tl)
        f_abef.append(fx)
        f_weight.append(len(candidate.split(' ')))
        print("Score: %s \t Candidate: %s" % (fx, candidate))

        i += 1

    numerator = sum(f_abef[i]*f_weight[i] for i in range(len(f_abef)))
    denominator = sum(f_weight)
    print("F_AVAL: %s" % (numerator/denominator))


if __name__ == "__main__":
    main()
