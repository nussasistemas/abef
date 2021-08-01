class Sword:
    text = ''
    translation = ''
    translation_n = ''
    classification = ''
    classN = ''
    genre = ''
    number = ''
    degree = ''

    def __init__(self, word):
        self.text = word.text
        self.classification = word.classification
        self.translation = word.translations

    def get_classification(self, classes):
        x = []
        i = 0
        while i < len(classes):
            if self.classification == classes[i]:
                x.append(i)
            i = i + 1
        return x

    def get_translation(self, dictionary):
        i = 0
        while i < len(dictionary):
            if self.text == dictionary[i]:
                self.translation_n = i
            i = i + 1
        return self.translation_n
