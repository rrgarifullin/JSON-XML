import json
import xml.etree.ElementTree as ET


def count_letters(word):
    if len(word) < 7:
        return 0
    else:
        return 1


def parse_json():
    with open('newsafr.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        words = []
        for news in data['rss']['channel']['items']:
            news_text = news['description'].split()
            words.extend(news_text)
        words = list(filter(count_letters, words))
        word_count_list = get_top_words(words)
        print_top_words(word_count_list, 'json')


def parse_xml():
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()
    news_list = root.findall('channel/item')
    words = []
    for news in news_list:
        description = news.find('description').text
        news_text = description.split()
        words.extend(news_text)
    words = list(filter(count_letters, words))
    word_count_list = get_top_words(words)
    print_top_words(word_count_list, 'xml')


def get_top_words(words):
    word_count = {}
    for word in words:
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count.update({word: 1})
    word_count_list = list(word_count.items())
    word_count_list.sort(key=lambda i: i[1], reverse=True)
    return word_count_list


def print_top_words(word_count_list, file):
    if file == 'json':
        print('\nТоп 10 самых встречающихся слов в newsafr.json: ')
    elif file == 'xml':
        print('\nТоп 10 самых встречающихся слов в newsafr.xml: ')
    for top_word in range(10):
        print(f'{word_count_list[top_word][0]} - {word_count_list[top_word][1]}')


parse_json()
parse_xml()