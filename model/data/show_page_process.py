from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import re

show_page = 'TheSeinfeldChronicles.htm'

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t for t in visible_texts)

def get_show_page_text(show_page):
    show_page_url = 'http://www.seinfeldscripts.com/{}'.format(show_page)
    print(show_page_url)
    html = urllib.request.urlopen(show_page_url).read()
    # print(text_from_html(html))
    show_text = text_from_html(html)
    return show_text


def get_show_text_dialogue(show_text):
    # splitting, as best I can figure, anywhere someone is listed as speaking...
    show_text_list = re.split('(\n(\s?)\w+:[\s\S]*?(?=(\n(\s?)\w+:)))', show_text)
    # stripping out extra space
    show_text_list_clean = [re.sub('\s+', ' ',x).strip() for x in show_text_list]
    # stripping out instances where the speakers name is copied (an artifact of the lookahead regex)
    show_text_list_clean = [re.sub('^\w+:$', '', x) for x in show_text_list_clean]
    show_text_list_clean = [x for x in show_text_list_clean if len(x) > 0 ]
    return show_text_list_clean


def extract_speaker_match(in_string):
    # extract speaker part
    speaker_search = re.search('^\w+:', in_string, re.IGNORECASE)
    if speaker_search:
        # print(speaker_search)
        return speaker_search.group(0)
    else:
        return None

def get_speaker_and_dialogue_lists(show_text_list_clean):
    # get speaker as list
    show_text_list_clean_speaker = [extract_speaker_match(x) for x in show_text_list_clean]
    # get dialogue as list
    show_text_list_clean_line = [re.sub('^\w+:', '', x).strip() for x in show_text_list_clean]
    return show_text_list_clean_speaker, show_text_list_clean_line

def get_show_text_speaker_dialogue_wrapper(show_page):
    show_text = get_show_page_text(show_page)
    show_text_list_clean = get_show_text_dialogue(show_text)
    show_text_list_clean_speaker, show_text_list_clean_line = get_speaker_and_dialogue_lists(show_text_list_clean)
    return show_text, show_text_list_clean_speaker, show_text_list_clean_line





