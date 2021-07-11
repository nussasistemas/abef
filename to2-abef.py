import os
import numpy
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
    i = 0
    #print (" - - - - - - - - - - - - - - - - - - - - - - -")
    #print ("Total de {} palavras".format(cont_palavras))
    #print ("ef_comparar: {} ".format(ef_comparar))

    while i < cont_palavras :
        #print("Palavra: {} ({})".format(t_c[i].text,t_c[i].classification))
        if t_c[i].classification in ef_comparar :
            cont_pc += 1
            #print(len(buscarTraducao(t_o,t_c[i],io)))
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
    "adjetivo"    :"a",
    "adverbio"    :"b",
    "artigo"      :"c",
    "conjuncao"   :"d",
    "interjeicao" :"e",
    "numeral"     :"f",
    "preposicao"  :"g",
    "pronome"     :"h",
    "substantivo" :"i",
    "verbo"       :"j",
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
    'a' : "the",
    'o' : "the",
    'da' : "of,to,from,than",
    'do' : "of,to,from,than",
    'de' : "of,to,from,in,whit,than",
    'camisa' : "shirt,sart,jacket",
    'é' : "is",
    'está' : "is",
    'este' : 'this',
    'isto' : 'this',
    'esta' : 'this',
    'preto' : 'black',
    'preta' : 'black',
    'branco' : "white,blank",
    'manga' : 'mango,sleeve',
    'rasgou' : 'rent,tore,ripped,lacerated',
    'rasgada': 'torn',
    "se" : "if",
    "você" : "you",
    "tu" : "you",
    "não" : "no,not,dont",
    "encontrar" : "meet,find,encounter,detect",
    "um" : "a,one,some",
    "uma" : "a,one,some",
    "jeito" : "way",
    "ganhar" : "earn,make",
    "ganhares" : "make,earn,get,gain,win",
    "ganhardes" : "make,earn,get,gain,win",
    "enquanto" : "while,whiles",
    "quando" : "when",
    "dorme" : "sleep,rest,li,kip,doss",
    "vai" : "will",
    "irá" : "will",
    "trabalhar" : "work",
    "trabalhará" : "work",
    "trabalharás" : "work",
    "trabalhares" : "work",
    "até" : "until,to,till",
    "morrer" : "die",
    "fazer" : "do,make,produce",
    "dinheiro" : "money",
    "forma" : "means,way",
    "caminho" : "path,way,road",
    "para" : "to,for,in,onto",
    "meio" : "way,half,means",
    "criar" : "create,make,get",


}

dicionario_en_pt = {
    'the' : "o,a,os,as",
    'can' : "pode,lata,recipiente",
    'short' : "bermuda,pequeno",
    'black' : "preto,preta",
    'this' : "isto,este,esta",
    'shirt' : "camisa",
    'sleeve' : "manga",
    'collar' : "gola",
    'is' : "é,está",
    'tore' : "rasgou",
    'torn' : "rasgada",
    'rent' : "rasgou",
    'lacerated' : "rasgou",
    'ripped' : "rasgou",
    "of" : "do,da,de",
    "to" : "do,da,de,para",
    "from" : "do,da,de",
    "than" : "do,da,de",
    "whit" : "de",
    "has" : "tem",
    "if" : "se,embora",
    "you" : "você,tu",
    "dont" : "não",
    "find" : "achar,encontrar,encontrares",
    "a" : "um,uma",
    "way" : "jeito,forma,maneira,meio,caminho",
    "make" : "fazer,criar,ganhar,ganhares,ganhardes",
    "money" : "dinheiro",
    "while" : "enquanto,durante,quando",
    "sleep" : "dorme,dormir,dormindo,dormes",
    "will" : "irá,vai",
    "work" : "trabalhar,trabalharás,trabalhares,trabalhará",
    "until" : "até",
    "die" : "morrer"
}

dic_ef_pt_to_en = {
    "cija":"cija,cia",
    "cidij":"ciij,cidcij",
}

dic_ef_en_to_pt = {
    "cija":"cija",
    "ciij":"cidij",
    "cidcij":"cidij",
    "iij":"cidij",
    "dhbjcigjidhj":"dhbjcigjidhj,dbjcigjidj,dhbjcigjidj",
    "hjjghj":"hjjgj,hjjghj,hjghj,hjgj,hjjgghj,jgj",
}

# -- Frases Idioma Origem I_o
frase_o = 'if you dont find a way to make money while you sleep, you will work until you die'
frase_o = frase_o.split(' ')

t_o = [] # Primeira parte do período
t_o.append(SWord('if','d'))
t_o.append(SWord('you','h'))
t_o.append(SWord('dont','b'))
t_o.append(SWord('find','j'))
t_o.append(SWord('a','c'))
t_o.append(SWord('way','i'))
t_o.append(SWord('to','g'))
t_o.append(SWord('make','j'))
t_o.append(SWord('money','i'))
t_o.append(SWord('while','d'))
t_o.append(SWord('you','h'))
t_o.append(SWord('sleep','j'))

t_o1 = [] # Segunda parte do período
t_o1.append(SWord('you','h'))
t_o1.append(SWord('will','j'))
t_o1.append(SWord('work','j'))
t_o1.append(SWord('until','g'))
t_o1.append(SWord('you','h'))
t_o1.append(SWord('die','j'))


# -- Frase Idioma Alvo I_a
frase_t = "se não achar um jeito de fazer dinheiro enquanto dorme, trabalhará até morrer"
frase_t = frase_t.split(' ')

t_t = [] # Primeira parte do período
t_t.append(SWord('se','d'))
t_t.append(SWord('não','b'))
t_t.append(SWord('achar','j'))
t_t.append(SWord('um','c'))
t_t.append(SWord('jeito','i'))
t_t.append(SWord('de','g'))
t_t.append(SWord('fazer','j'))
t_t.append(SWord('dinheiro','i'))
t_t.append(SWord('enquanto','d'))
t_t.append(SWord('dorme','j'))

t_t1 = [] # Segunda parte do período
t_t1.append(SWord('trabalhará','j'))
t_t1.append(SWord('até','g'))
t_t1.append(SWord('morrer','j'))

# -- Neste ponto, comparar a EFt
# Parte 1
ef_io_ia = getEFAlvo(getEFString(t_o),dic_ef_en_to_pt)
ef_t = getEFString(t_t)
ef_comparar = getEFMaisProximo(ef_t,ef_io_ia)
Fx_EF = avalEF(ef_t,ef_io_ia[ef_comparar])
score = avalFrase(t_t,t_o,ef_io_ia[ef_comparar],'en',Fx_EF)

# Parte 2
ef_io_ia = getEFAlvo(getEFString(t_o1),dic_ef_en_to_pt)
ef_t = getEFString(t_t1)
ef_comparar = getEFMaisProximo(ef_t,ef_io_ia)
Fx_EF1 = avalEF(ef_t,ef_io_ia[ef_comparar])
score1 = avalFrase(t_t1,t_o1,ef_io_ia[ef_comparar],'en',Fx_EF1)

print("Candidato {}({})".format(1,((score*len(t_o))+(score1*len(t_o1)))/(len(t_o)+len(t_o1))))


# -- Frase Idioma Alvo I_a
frase_t = "você irá trabalhar até morrer, se não achar um jeito de ganhar dinheiro enquanto dorme"
frase_t = frase_t.split(' ')

t_t = [] # Primeira parte do período
t_t.append(SWord('você','h'))
t_t.append(SWord('irá','j'))
t_t.append(SWord('trabalhar','j'))
t_t.append(SWord('até','g'))
t_t.append(SWord('morrer','j'))

t_t1 = [] # Segunda parte do período
t_t1.append(SWord('se','d'))
t_t1.append(SWord('não','b'))
t_t1.append(SWord('achar','j'))
t_t1.append(SWord('um','c'))
t_t1.append(SWord('jeito','i'))
t_t1.append(SWord('de','g'))
t_t1.append(SWord('fazer','j'))
t_t1.append(SWord('dinheiro','i'))
t_t1.append(SWord('enquanto','d'))
t_t1.append(SWord('dorme','j'))

# -- Neste ponto, comparar a EFt
# Parte 1
ef_io_ia = getEFAlvo(getEFString(t_o),dic_ef_en_to_pt)
ef_t = getEFString(t_t)
ef_comparar = getEFMaisProximo(ef_t,ef_io_ia)
Fx_EF = avalEF(ef_t,ef_io_ia[ef_comparar])
score = avalFrase(t_t,t_o,ef_io_ia[ef_comparar],'en',Fx_EF)

# Parte 2
ef_io_ia = getEFAlvo(getEFString(t_o1),dic_ef_en_to_pt)
ef_t = getEFString(t_t1)
ef_comparar = getEFMaisProximo(ef_t,ef_io_ia)
Fx_EF1 = avalEF(ef_t,ef_io_ia[ef_comparar])
score1 = avalFrase(t_t1,t_o1,ef_io_ia[ef_comparar],'en',Fx_EF1)

print("Candidato {}({})".format(2,((score*len(t_o))+(score1*len(t_o1)))/(len(t_o)+len(t_o1))))

# -- Frase Idioma Alvo I_a
frase_t = "se tu não encontrares uma forma de ganhar dinheiro enquanto dormes, trabalharás até morrer"
frase_t = frase_t.split(' ')

t_t = [] # Primeira parte do período
t_t.append(SWord('se','d'))
t_t.append(SWord('tu','h'))
t_t.append(SWord('não','b'))
t_t.append(SWord('encontrares','j'))
t_t.append(SWord('uma','c'))
t_t.append(SWord('forma','i'))
t_t.append(SWord('de','g'))
t_t.append(SWord('ganhar','j'))
t_t.append(SWord('dinheiro','i'))
t_t.append(SWord('enquanto','d'))
t_t.append(SWord('dormes','j'))

t_t1 = [] # Segunda parte do período
t_t1.append(SWord('trabalharás','j'))
t_t1.append(SWord('até','g'))
t_t1.append(SWord('morrer','j'))

# -- Neste ponto, comparar a EFt
# Parte 1
ef_io_ia = getEFAlvo(getEFString(t_o),dic_ef_en_to_pt)
ef_t = getEFString(t_t)
ef_comparar = getEFMaisProximo(ef_t,ef_io_ia)
Fx_EF = avalEF(ef_t,ef_io_ia[ef_comparar])
score = avalFrase(t_t,t_o,ef_io_ia[ef_comparar],'en',Fx_EF)

# Parte 2
ef_io_ia = getEFAlvo(getEFString(t_o1),dic_ef_en_to_pt)
ef_t = getEFString(t_t1)
ef_comparar = getEFMaisProximo(ef_t,ef_io_ia)
Fx_EF1 = avalEF(ef_t,ef_io_ia[ef_comparar])
score1 = avalFrase(t_t1,t_o1,ef_io_ia[ef_comparar],'en',Fx_EF1)

print("Candidato {}({})".format(3,((score*len(t_o))+(score1*len(t_o1)))/(len(t_o)+len(t_o1))))

# -- Frase Idioma Alvo I_a
frase_t = "se você não encontrar um caminho para fazer dinheiro enquanto você dorme, você trabalhará até você morrer"
frase_t = frase_t.split(' ')

t_t = [] # Primeira parte do período
t_t.append(SWord('se','d'))
t_t.append(SWord('você','h'))
t_t.append(SWord('não','b'))
t_t.append(SWord('encontrar','j'))
t_t.append(SWord('um','c'))
t_t.append(SWord('caminho','i'))
t_t.append(SWord('para','g'))
t_t.append(SWord('fazer','j'))
t_t.append(SWord('dinheiro','i'))
t_t.append(SWord('enquanto','d'))
t_t.append(SWord('você','h'))
t_t.append(SWord('dorme','j'))

t_t1 = [] # Segunda parte do período
t_t1.append(SWord('você','h'))
t_t1.append(SWord('trabalhará','j'))
t_t1.append(SWord('até','g'))
t_t1.append(SWord('você','h'))
t_t1.append(SWord('morrer','j'))

# -- Neste ponto, comparar a EFt
# Parte 1
ef_io_ia = getEFAlvo(getEFString(t_o),dic_ef_en_to_pt)
ef_t = getEFString(t_t)
ef_comparar = getEFMaisProximo(ef_t,ef_io_ia)
Fx_EF = avalEF(ef_t,ef_io_ia[ef_comparar])
score = avalFrase(t_t,t_o,ef_io_ia[ef_comparar],'en',Fx_EF)

# Parte 2
ef_io_ia = getEFAlvo(getEFString(t_o1),dic_ef_en_to_pt)
ef_t = getEFString(t_t1)
ef_comparar = getEFMaisProximo(ef_t,ef_io_ia)
Fx_EF1 = avalEF(ef_t,ef_io_ia[ef_comparar])
score1 = avalFrase(t_t1,t_o1,ef_io_ia[ef_comparar],'en',Fx_EF1)

print("Candidato {}({})".format(4,((score*len(t_o))+(score1*len(t_o1)))/(len(t_o)+len(t_o1))))

# -- Frase Idioma Alvo I_a
frase_t = "se não encontrar você meio para criar dinheiro quando dorme você, trabalhar até morrer você irá"
frase_t = frase_t.split(' ')

t_t = [] # Primeira parte do período
t_t.append(SWord('se','d'))
t_t.append(SWord('não','b'))
t_t.append(SWord('encontrar','j'))
t_t.append(SWord('você','h'))
t_t.append(SWord('meio','i'))
t_t.append(SWord('para','g'))
t_t.append(SWord('criar','j'))
t_t.append(SWord('dinheiro','i'))
t_t.append(SWord('quando','d'))
t_t.append(SWord('dorme','j'))
t_t.append(SWord('você','h'))

t_t1 = [] # Segunda parte do período
t_t1.append(SWord('trabalhar','j'))
t_t1.append(SWord('até','g'))
t_t1.append(SWord('morrer','j'))
t_t1.append(SWord('você','h'))
t_t1.append(SWord('irá','j'))

# -- Neste ponto, comparar a EFt
# Parte 1
ef_io_ia = getEFAlvo(getEFString(t_o),dic_ef_en_to_pt)
ef_t = getEFString(t_t)
ef_comparar = getEFMaisProximo(ef_t,ef_io_ia)
Fx_EF = avalEF(ef_t,ef_io_ia[ef_comparar])
score = avalFrase(t_t,t_o,ef_io_ia[ef_comparar],'en',Fx_EF)

# Parte 2
ef_io_ia = getEFAlvo(getEFString(t_o1),dic_ef_en_to_pt)
ef_t = getEFString(t_t1)
ef_comparar = getEFMaisProximo(ef_t,ef_io_ia)
Fx_EF1 = avalEF(ef_t,ef_io_ia[ef_comparar])
score1 = avalFrase(t_t1,t_o1,ef_io_ia[ef_comparar],'en',Fx_EF1)

print("Candidato {}({})".format(5,((score*len(t_o))+(score1*len(t_o1)))/(len(t_o)+len(t_o1))))

# -- Frase Idioma Alvo I_a
frase_t = "se você não encontrar um jeito de ganhar dinheiro enquanto dorme, você vai trabalhar até morrer"
frase_t = frase_t.split(' ')

t_t = [] # Primeira parte do período
t_t.append(SWord('se','d'))
t_t.append(SWord('você','h'))
t_t.append(SWord('não','b'))
t_t.append(SWord('encontrar','j'))
t_t.append(SWord('um','c'))
t_t.append(SWord('jeito','i'))
t_t.append(SWord('de','g'))
t_t.append(SWord('ganhar','j'))
t_t.append(SWord('dinheiro','i'))
t_t.append(SWord('enquanto','d'))
t_t.append(SWord('dorme','j'))

t_t1 = [] # Segunda parte do período
t_t1.append(SWord('você','h'))
t_t1.append(SWord('vai','j'))
t_t1.append(SWord('trabalhar','j'))
t_t1.append(SWord('até','g'))
t_t1.append(SWord('morrer','j'))

# -- Neste ponto, comparar a EFt
# Parte 1
ef_io_ia = getEFAlvo(getEFString(t_o),dic_ef_en_to_pt)
ef_t = getEFString(t_t)
ef_comparar = getEFMaisProximo(ef_t,ef_io_ia)
Fx_EF = avalEF(ef_t,ef_io_ia[ef_comparar])
score = avalFrase(t_t,t_o,ef_io_ia[ef_comparar],'en',Fx_EF)

# Parte 2
ef_io_ia = getEFAlvo(getEFString(t_o1),dic_ef_en_to_pt)
ef_t = getEFString(t_t1)
ef_comparar = getEFMaisProximo(ef_t,ef_io_ia)
Fx_EF1 = avalEF(ef_t,ef_io_ia[ef_comparar])
score1 = avalFrase(t_t1,t_o1,ef_io_ia[ef_comparar],'en',Fx_EF1)

print("Candidato {}({})".format(6,((score*len(t_o))+(score1*len(t_o1)))/(len(t_o)+len(t_o1))))