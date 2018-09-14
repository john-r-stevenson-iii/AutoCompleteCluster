from bs4 import BeautifulSoup
import urllib.request
import json
import time
import re

from show_page_process import get_show_text_speaker_dialogue_wrapper

resp = urllib.request.urlopen("http://www.seinfeldscripts.com/seinfeld-scripts.html")
soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))

link_list = []
for link in soup.find_all('a', href=True):
    print(link['href'])
    link_list.append(link['href'].strip())

# print(link_list[:20])

# I manually looked at which ones were the first and last here
start_url = 'TheSeinfeldChronicles.htm'
end_url = 'TheFinale.htm'

# get indexes for the first and last shows in the list of links
target_startindex = link_list.index(start_url)
target_endindex = link_list.index(end_url)

# show links
show_link_list = link_list[target_startindex:target_endindex]
# print(show_link_list[:10])

for show in show_link_list:
    pretty_name = re.sub('\.htm(l)?', '', show)
    try:
        show_text, show_text_list_clean_speaker, show_text_list_clean_line = get_show_text_speaker_dialogue_wrapper(show)
    except:
        print('could not get show: {}'.format(show))
    try:
        with open('./scripts/raw_text/{}.txt'.format(pretty_name), 'w') as f:
            f.write(show_text)
            f.close()
    except:
        print('could not write show text: {}'.format(show))
    try:
        out_dict = {"speaker_array":show_text_list_clean_speaker,
                    "dialogue_array":show_text_list_clean_line}

        with open('./scripts/formatted_dialogues/{}.json'.format(pretty_name), "w") as write_file:
            json.dump(out_dict, write_file, indent=2)
            write_file.close()
    except:
        print('could not write json for: {}'.format(show))
    time.sleep(2)



