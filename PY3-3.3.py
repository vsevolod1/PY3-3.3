import requests

KEY = 'trnsl.1.1.20170330T165215Z.8f2572a45578ae5f.efcf9b1afa81dd18491f836c4e630b284c834770'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

# функция для чтения файла и записи его в переменную
def file_to_str(file):
    text_to_translate = ''
    with open(file, 'r') as f:
        for line in f:
            text_to_translate += line
    return text_to_translate

# функция для записи строки в файл
def str_to_file(text, file):
    with open(file, 'w') as f:
        f.write(text)

# функция перевода
def translate_it(text, from_lang, to_lang='ru'):

    params = {
        'key': KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }

    response = requests.get(URL, params=params)
    return ''.join(response.json()['text'])

# функция читает исходный файл, переводит и записыват в указанный файл
def translate_to_file(input_file, output_file, from_lang, to_lang='ru'):
    input_text = file_to_str(input_file)
    translated_text = translate_it(input_text, from_lang, to_lang)
    str_to_file(translated_text, output_file)

translate_to_file('./input files/FR.txt', './output files/FR.txt', 'fr')
