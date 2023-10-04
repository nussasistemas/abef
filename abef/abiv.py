import os
import numpy
import nltk
import random
import editdistance # -- Levenshtein distance algorithm

os.system("clear") # Clear last results in screen

ptbrWords = []
enWords = []
original_sentence = []

# Program principal da métrica ABIV RTBE

# Retorna cadeira de caracteres separadas por hifens a esturura frasal de uma frase 
def getEFString(frase):
    ef = ''
    sep = ''
    i = 0
    while i < len(frase):
        if i > 0:
            ef += sep+frase[i].classification
        else:
            ef += frase[i].classification
        i = i + 1
    return ef

def getEFAlvo(ef,dicionario):
    if ef in dicionario:
        return dicionario[ef].split(',')
    else:
        return []

def getEFMaisProximo(ef,ef_ref):
    ef_c = 0
    distance = 0
    menor = 10000000
    i = 0 
    while i < len(ef_ref):
        distance = editdistance.eval(ef,ef_ref[i])
        if distance < menor:
            menor = distance
            ef_c = i
        i = i + 1
    return ef_c

def avalEF(ef,ef_ref):
    ef_c = len(ef)
    distance = editdistance.eval(ef,ef_ref)
    return (ef_c - distance)/ef_c

def getTranslation(palavra,io) :
    if io == 'en' :
        dic = dicionario_en_pt
    else :
        dic = dicionario_pt_en
    if palavra in dic:
        return dic[palavra].split(',')
    else :
        return []

def buscarTraducao(t_o,palavra,io) :
    i = 0
    posicoes = []

    while i<len(t_o):
        if t_o[i].classification == palavra.classification :
            if palavra.text in getTranslation(t_o[i].text,io):
                posicoes.append(i)
        i = i + 1
    return posicoes

def avalFrase(t_c,t_o,ef_ref,io,Fx_EF):
    ef_comparar = [x for x in ef_ref]
    cont_palavras = len(t_c)
    cont_pc = 0
    fx = 0
    pnldd = 0
    i = 0
    #print (" - - - - - - - - - - - - - - - - - - - - - - -")
    #print ("Total de {} palavras".format(cont_palavras))
    #print ("ef_comparar: {} ".format(ef_comparar))

    while i < cont_palavras :
        #print("Palavra: {} ({})".format(t_c[i].text,t_c[i].classification))
        if t_c[i].classification in ef_comparar :
            cont_pc += 1
            if len(buscarTraducao(t_o,t_c[i],io)) > 0 :
                fx += 1 
        i = i+1 
    return (fx/(cont_pc*1.0))*Fx_EF


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

    def __init__(self,text,classification):
        self.text = text
        self.classification = classification

    def get_classification(self,classes):
        x = []
        i=0
        while i < len(classes):
            if (self.classification == classes[i]):
                x.append(i)
            i = i+1
        return x

    def get_translation(self,dictionary):
        i=0
        while i< len(dictionary):
            if (self.text == dictionary[i]) :
                self.translationN = i
            i = i+1 
        return self.translationN
    
""" 

    PROGRAMA PRINCIPAL

 """

# -- Classes de palavras
class_p = {
    "adjetivo":"a",
    "adverbio":"b",
    "artico":"c",
    "conjuncao":"d",
    "interjeicao":"e",
    "numeral":"f",
    "preposicao":"g",
    "pronome":"h",
    "substantivo":"i",
    "verbo":"j"
}
class_pesos = {
    'a' : 0.7, 
    'b' : 0.3, 
    'c' : 0.3, 
    'd' : 0.3, 
    'e' : 0.3, 
    'f' : 0.3, 
    'g' : 0.3, 
    'h' : 0.3, 
    'i' : 0.7, 
    'j' : 0.7
}

# -- Dicionários 
dicionario_pt_en = {
    'o' : "the",
    'cavalo' : "horse",
    'é' : "is",
    'este' : 'this',
    'isto' : 'this',
    'esta' : 'this',
    'preto' : 'black',
    'preta' : 'black',
    'branco' : "white,blank"
}

dicionario_en_pt = {
    'the' : "o,a,os,as",
    'chicken' : "frango",
    'black' : "preto,preta",
    'this' : "isto,este,esta",
    'horse' : "cavalo",
    'is' : "é,está",
    'white' : "branco,branca,brancos,brancas"
}

dic_ef_pt_to_en = {
    "cija":"cija,cia"
}

dic_ef_en_to_pt = {
    "cija":"cija"
}

# -- Frases Idioma Origem I_o
frase_o = 'o cavalo é branco'
frase_o = frase_o.split(' ')
t_o = []
t_o.append(SWord('o','c'))
t_o.append(SWord('cavalo','i'))
t_o.append(SWord('é','j'))
t_o.append(SWord('branco','a'))

# -- Frase Idioma Alvo I_a
frase_t = 'the horse is white'
frase_t = frase_t.split(' ')
t_t = []

t_t.append(SWord('the','c'))
t_t.append(SWord('horse','i'))
t_t.append(SWord('is','j'))
t_t.append(SWord('white','a'))

# -- Neste ponto, comparar a EFt
ef_io_ia = getEFAlvo(getEFString(t_o),dic_ef_pt_to_en)
#ef_t = getEFString(t_t)
#ef_comparar = getEFMaisProximo(ef_t,ef_io_ia)
#Fx_EF = avalEF(ef_t,ef_io_ia[ef_comparar])
#Fx_EF = avalEF(ef_t,'ajic')

# -- Imprime os resultados para análise
#print ("T_o: {}".format(frase_o))
#print ("T_t: {}".format(frase_t))
#print ("EF_ref: {}".format(ef_io_ia))
#print ("EF_comparar: {}".format(ef_io_ia[ef_comparar]))
#print ("Fx_EF: {}".format(Fx_EF))
#print ("Fx_T_t: {}".format(avalFrase(t_t,t_o,ef_io_ia[ef_comparar],'pt',Fx_EF)))

candidates = ["the white horse","the chicken is white","the the the the","this horse is black","white horse is the"]

t_t = []
t_t.append(SWord('the','c'))
t_t.append(SWord('white','a'))
t_t.append(SWord('horse','i'))
ef_t = getEFString(t_t)
ef_comparar = getEFMaisProximo(ef_t,ef_io_ia)
Fx_EF = avalEF(ef_t,ef_io_ia[ef_comparar])
score = avalFrase(t_t,t_o,ef_io_ia[ef_comparar],'pt',Fx_EF)
print("Candidato {}({})".format(1,score))

t_t = []
t_t.append(SWord('the','c'))
t_t.append(SWord('chicken','i'))
t_t.append(SWord('is','j'))
t_t.append(SWord('white','a'))
ef_t = getEFString(t_t)
ef_comparar = getEFMaisProximo(ef_t,ef_io_ia)
Fx_EF = avalEF(ef_t,ef_io_ia[ef_comparar])
score = avalFrase(t_t,t_o,ef_io_ia[ef_comparar],'pt',Fx_EF)
print("Candidato {}({})".format(2,score))

t_t = []
t_t.append(SWord('the','c'))
t_t.append(SWord('the','c'))
t_t.append(SWord('the','c'))
t_t.append(SWord('the','c'))
ef_t = getEFString(t_t)
ef_comparar = getEFMaisProximo(ef_t,ef_io_ia)
Fx_EF = avalEF(ef_t,ef_io_ia[ef_comparar])
score = avalFrase(t_t,t_o,ef_io_ia[ef_comparar],'pt',Fx_EF)
print("Candidato {}({})".format(3,score))

t_t = []
t_t.append(SWord('this','c'))
t_t.append(SWord('horse','i'))
t_t.append(SWord('is','j'))
t_t.append(SWord('black','a'))
ef_t = getEFString(t_t)
ef_comparar = getEFMaisProximo(ef_t,ef_io_ia)
Fx_EF = avalEF(ef_t,ef_io_ia[ef_comparar])
score = avalFrase(t_t,t_o,ef_io_ia[ef_comparar],'pt',Fx_EF)
print("Candidato {}({})".format(4,score))

t_t = []
t_t.append(SWord('white','a'))
t_t.append(SWord('horse','i'))
t_t.append(SWord('is','j'))
t_t.append(SWord('the','c'))

ef_t = getEFString(t_t)
ef_comparar = getEFMaisProximo(ef_t,ef_io_ia)
Fx_EF = avalEF(ef_t,ef_io_ia[ef_comparar])
score = avalFrase(t_t,t_o,ef_io_ia[ef_comparar],'pt',Fx_EF)
print("Candidato {}({})".format(5,score))

t_t = []
t_t.append(SWord('the','c'))
t_t.append(SWord('horse','i'))
t_t.append(SWord('is','j'))
t_t.append(SWord('white','a'))
ef_t = getEFString(t_t)
ef_comparar = getEFMaisProximo(ef_t,ef_io_ia)
Fx_EF = avalEF(ef_t,ef_io_ia[ef_comparar])
score = avalFrase(t_t,t_o,ef_io_ia[ef_comparar],'pt',Fx_EF)
print("Candidato {}({})".format(6,score))