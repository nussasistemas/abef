# -- Levenshtein distance algorithm
import editdistance


def getEFString(frase):
    ef = ''
    sep = ''
    i = 0
    while i < len(frase):
        if i > 0:
            ef += sep + frase[i].classification
        else:
            ef += frase[i].classification
        i = i + 1
    return ef


def getEFAlvo(ef, dicionario):
    if ef in dicionario:
        return dicionario[ef].split(',')
    else:
        return []


def getEFMaisProximo(ef, ef_ref):
    ef_c = 0
    distance = 0
    menor = 10000000
    i = 0
    while i < len(ef_ref):
        distance = editdistance.eval(ef, ef_ref[i])
        if distance < menor:
            menor = distance
            ef_c = i
        i = i + 1
    return ef_c


def avalEF(ef, ef_ref):
    ef_c = len(ef)
    distance = editdistance.eval(ef, ef_ref)
    return (ef_c - distance) / ef_c


def getTranslation(palavra, io):
    if io == 'en':
        dic = dicionario_en_pt
    else:
        dic = dicionario_pt_en
    if palavra in dic:
        return dic[palavra].split(',')
    else:
        return []


def buscarTraducao(t_o, palavra, io):
    i = 0
    posicoes = []

    while i < len(t_o):
        if t_o[i].classification == palavra.classification:
            if palavra.text in getTranslation(t_o[i].text, io):
                posicoes.append(i)
        i = i + 1
    return posicoes


def avalFrase(t_c, t_o, ef_ref, io, Fx_EF):
    ef_comparar = [x for x in ef_ref]
    cont_palavras = len(t_c)
    cont_pc = 0
    fx = 0
    pnldd = 1
    i = 0
    # print (" - - - - - - - - - - - - - - - - - - - - - - -")
    # print ("Total de {} palavras".format(cont_palavras))
    # print ("ef_comparar: {} ".format(ef_comparar))

    # Calcula penalidade por repeticão de palavras
    if Fx_EF < 1:
        words_list = [w.text for w in t_c]
        repetitions = {i: words_list.count(i) for i in words_list}
        pnldd = len(repetitions)/len(words_list)
        print("Lista: %s / %s" % (repetitions, pnldd))


    while i < cont_palavras:
        # print("Palavra: {} ({})".format(t_c[i].text,t_c[i].classification))
        if t_c[i].classification in ef_comparar:
            cont_pc += 1
            if len(buscarTraducao(t_o, t_c[i], io)) > 0:
                fx += 1
        i = i + 1
    return (fx / (cont_pc * 1.0)) * Fx_EF * pnldd


class SWord:
    """Classe de palavras para tradutor"""
    text = ''
    translation = ''
    translationN = ''
    classification = ''
    classN = ''
    genre = ''
    number = ''
    degree = ''

    def __init__(self, text, classification):
        self.text = text
        self.classification = classification

    def get_classification(self, classes):
        x = []
        i = 0
        while i < len(classes):
            if (self.classification == classes[i]):
                x.append(i)
            i = i + 1
        return x

    def get_translation(self, dictionary):
        i = 0
        while i < len(dictionary):
            if (self.text == dictionary[i]):
                self.translationN = i
            i = i + 1
        return self.translationN