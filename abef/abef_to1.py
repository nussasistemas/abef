import yaml
from data.class_weights import Class_Weights
from lib.abef import Abef


def load_parameters(path):
    with open(path, 'r') as file:
        return yaml.full_load(file)


def evaluate(t_o, candidate, abef, source_language, dictionary, dict_ss_sl_tl):
    sentence_t = candidate.split(' ')
    t_t = []

    for word in sentence_t:
        t_t.append(dictionary['words'][word])

    ss_sl_tl = abef.get_ss_target(abef.get_ss_string(t_o), dict_ss_sl_tl)
    ss_t = abef.get_ss_string(t_t)
    ss = abef.get_nearest_ss(ss_t, ss_sl_tl)
    fx_ss = abef.aval_ss(ss_t, ss_sl_tl[ss])
    return abef.aval_sentence(t_t, t_o, ss_sl_tl[ss], source_language, fx_ss)


def main():
    dict_pt_en = load_parameters('./data/dictionary_pt_en.yml')
    dict_en_pt = load_parameters('./data/dictionary_en_pt.yml')
    ss_pt_en = load_parameters('./data/ss_pt_en.yml')
    ss_en_pt = load_parameters('./data/ss_en_pt.yml')

    sentence_o = 'o cavalo é branco'.split(' ')
    candidates = [
        "the white horse",
        "the chicken is white",
        "the the the the",
        "this horse is black",
        "white horse is the",
        "the horse is white",
    ]

    t_o = []
    for word in sentence_o:
        t_o.append(dict_pt_en['words'][word])

    class_penalties = ['i', 'j']
    source_language = 'pt'
    target_language = 'en'
    abef = Abef(dict_pt_en['words'], dict_en_pt['words'], source_language, target_language, Class_Weights, class_penalties)

    i = 0
    for candidate in candidates:
        evaluation = evaluate(t_o, candidate, abef, source_language, dict_en_pt, ss_pt_en)
        print("Candidato %d: %.5f" % (i+1, evaluation))
        i += 1


if __name__ == "__main__":
    main()
