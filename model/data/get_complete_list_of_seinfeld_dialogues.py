import json
from os import walk
import pandas as pd
import re

mypath = './scripts/formatted_dialogues/'
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break




script_list = []
base_speaker_array = []
base_dialogue_array = []
for file in f:
    print(file)
    with open(mypath+file, 'r') as in_json:
        in_dict = json.load(in_json)
    speaker_array = in_dict['speaker_array'][1:]
    speaker_array = [x.upper() for x in speaker_array]
    dialogue_array = in_dict['dialogue_array'][1:]
    base_speaker_array.extend(speaker_array)
    base_dialogue_array.extend(dialogue_array)


out_df = pd.DataFrame()
out_df['speaker'] = base_speaker_array
out_df['dialogue'] = base_dialogue_array
dialogue_clean = out_df['dialogue'].apply(lambda x: re.sub('(\(|\[).*?(\)|\])', '', x))

out_df['dialogue_clean'] = dialogue_clean


out_df.to_csv('./scripts/clean_scripts.csv')