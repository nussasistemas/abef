import os

# Bibliotecas necessárias
from lib.dictionary import *
from lib.translating import *

os.system("clear")

# Programa principal para tradução
lang_from = 'en'
lang_to = 'pt'

# ---    Texto a ser traduzido ---

dictionary_words = ''
text_original = '' # T_O
text_translated = '' # T_T

text_original = 'The fur of the white horse is white'
text_reference = 'O pêlo do cavalo branco é branco'

dictionary_words = dictionary(text_original,text_reference)
#print(dictionary_words)
r = translating(text_original,lang_from,lang_to)
print(r)