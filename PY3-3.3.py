import requests


key = 'trnsl.1.1.20170330T165215Z.8f2572a45578ae5f.efcf9b1afa81dd18491f836c4e630b284c834770'
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text, from_lang, to_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """

    params = {
        'key': key,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }

    response = requests.get(url, params=params)
    return ''.join(response.json()['text'])

def file_to_str (file):
    text_to_translate = ''
    with open(file, 'r') as f:
        for line in f:
            text_to_translate += line
    return text_to_translate

def str_to_file (translated_text, file):
    with open(file, 'w') as f:
        f.write(translated_text)
translated_text = (translate_it(file_to_str('./input files/ES.txt'), 'es', 'ru'))
print(translated_text)
print(type(translated_text))

str_to_file(translated_text, './output files/ES.txt')
# print(translate_it('Что это такое?', 'de'))
