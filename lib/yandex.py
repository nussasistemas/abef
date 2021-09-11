import requests
import yaml
import time
from termcolor import colored

def load_parameters(path):
    with open(path, 'r') as file:
        return yaml.full_load(file)

def_dict = {
    'adjective': 'a',
    'adverb': 'b',
    'determiner': 'c',
    'conjunction': 'd',
    'interjection': 'e',
    'preposition': 'g',
    'pronoun': 'h',
    'noun': 'i',
    'verb': 'j'
}

class Yandex:
    api_name = "ABEF"
    api_key = "dict.1.1.20210911T131735Z.7a7f6311dc4ad6b0.2ce436020244ab5859cedb7df9efec6f8cc2aaee"
    api_url = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={}&lang={}&text={}"

    language_pair = "en-pt"

    def __init__(self, language_pair="en-pt"):
        self.language_pair = language_pair

    def call_request(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()

            if response.status_code == 200:
                results = response.json()
                if len(results['def']) > 0:
                    return response.json()
        except requests.exceptions.HTTPError as error:
            print(error)

        return False

    def get_word_data(self, word):
        if len(word) < 1:
            return []

        return self.call_request(self.api_url.format(self.api_key, self.language_pair, word))

    def run(self):
        # Words to be translated
        words = ['one']

        # dict_source = load_parameters('../data/dictionary_pt_en.yml')
        dict_source = load_parameters('../data/dictionary_en_pt.yml')

        # New words translated
        new_dict_words = {'words': {}}

        # Fetch every single word
        for word in words:
            # Check if the word already exists in dictionary
            if word not in dict_source['words']:
                print(colored('Translating: %s ' % word, 'blue'))

                results = self.get_word_data(word)

                if results:
                    print(colored('Mounting data...', 'blue'))
                    # Initiate a blank new word for receive the data
                    new_word = {'text': word, 'classification': [], 'translations': []}

                    # Seek for all definitions in the results
                    for value in results['def']:
                        new_word['classification'].append(def_dict[value['pos']])

                        # Seek for every translation
                        for translation in value['tr']:
                            new_word['translations'].append(translation['text'])

                            if 'syn' in translation:
                                # Seek for every synonym
                                for synonym in translation['syn']:
                                    new_word['translations'].append(synonym['text'])
                    new_dict_words['words'][word] = new_word
                else:
                    print(colored('No data found!', 'red'))

                # Give a break for the API
                print(colored('Waiting a sec...', 'magenta'))
                time.sleep(1)

        with open('../data/new_dict_values.yml', 'w') as yaml_file:
            yaml.dump(new_dict_words, yaml_file, default_flow_style=False)

        print(colored('   FINISHED!   ', 'green', attrs=['reverse']))
        print(new_dict_words)


if __name__ == "__main__":
    source_word = "sleeve"
    yandex = Yandex("en-pt")
    yandex.run()
