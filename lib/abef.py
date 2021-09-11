import sys
import editdistance


class Abef:
    dict_sl_tl = None  # Source Language to Target Language Dictionary
    dict_tl_sl = None  # Target Language to Source Language Dictionary
    source_language = None
    target_language = None
    class_weights = None
    class_penalties = None

    def __init__(self, dict_sl_tl, dict_tl_sl, source_language, target_language, class_weights=None,
                 class_penalties=None):
        if class_penalties is None:
            class_penalties = ['i', 'j']
        self.class_penalties = class_penalties
        self.class_weights = class_weights
        self.dict_sl_tl = dict_sl_tl
        self.dict_tl_sl = dict_tl_sl
        self.source_language = source_language
        self.target_language = target_language

    def get_ss_string(self, sentence):
        ss = ''
        sep = ''
        i = 0
        while i < len(sentence):
            if i > 0:
                ss += sep + sentence[i]['classification'][0]
            else:
                ss += sentence[i]['classification'][0]
            i = i + 1
        return ss

    def get_ss_target(self, ss, dictionary):
        if ss in dictionary:
            return dictionary[ss]
        else:
            return []

    def get_nearest_ss(self, ss, ss_ref):
        ss_count = 0
        smaller = sys.maxsize
        i = 0
        while i < len(ss_ref):
            distance = editdistance.eval(ss, ss_ref[i])
            if distance < smaller:
                smaller = distance
                ss_count = i
            i = i + 1
        return ss_count

    def aval_ss(self, ss, ss_ref):
        ss_count = len(ss)
        distance = editdistance.eval(ss, ss_ref)
        return (ss_count - distance) / ss_count

    def get_translation(self, word, source_language):
        if source_language == self.source_language:
            dictionary = self.dict_sl_tl
        else:
            dictionary = self.dict_tl_sl
        if word in dictionary:
            return dictionary[word]['translations']
        else:
            return []

    def search_translation(self, t_o, word, io):
        i = 0
        positions = []

        while i < len(t_o):
            if t_o[i]['classification'][0] == word['classification'][0]:
                if word['text'] in self.get_translation(t_o[i]['text'], io):
                    positions.append(i)
            i += 1
        return positions

    def aval_sentence(self, t_c, t_o, ss_ref, source_language, fx_ss):
        ss_compare = [x for x in ss_ref]
        count_words = len(t_c)
        count_pc = 0
        fx = 0
        penalty = 1
        i = 0

        if fx_ss < 1:
            words_list = [w['text'] for w in t_c]
            repetitions = {i: words_list.count(i) for i in words_list}
            penalty = len(repetitions) / len(words_list)

        while i < count_words:
            if t_c[i]['classification'][0] in ss_compare:
                count_pc += 1
                if len(self.search_translation(t_o, t_c[i], source_language)) > 0:
                    fx += 1
                else:
                    if t_c[i]['classification'][0] in self.class_penalties and self.class_weights is not None:
                        penalty *= 1 - self.class_weights[t_c[i]['classification'][0]]
            i = i + 1

        return (fx / (count_pc * 1.0)) * fx_ss * penalty if count_pc > 0 else count_pc
